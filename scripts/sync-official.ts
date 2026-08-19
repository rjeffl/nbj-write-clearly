// Vendors the Google Developer Documentation Style Guide pages linked from
// references/official-index.md into references/official/<slug>.md.
// Usage: bun scripts/sync-official.ts [--dry-run]
// Google licenses page content under CC BY 4.0 and code samples under
// Apache 2.0; each written file carries a source/license header. See NOTICE.md.

import { readFile, writeFile, mkdir } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { parse, type HTMLElement } from "node-html-parser";
import TurndownService from "turndown";
// @ts-expect-error turndown-plugin-gfm ships no type declarations
import { gfm } from "turndown-plugin-gfm";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const skillRoot = join(repoRoot, ".agents/skills/nbj-write-clearly");
const indexPath = join(skillRoot, "references/official-index.md");
const outDir = join(skillRoot, "references/official");

const REQUEST_DELAY_MS = 300;
const MIN_CONTENT_CHARS = 500;

// Devsite boilerplate that must not end up in the snapshots.
const STRIP_SELECTORS = [
  "style",
  "script",
  "devsite-feedback",
  "devsite-thumb-rating",
  "devsite-recommendations",
  "devsite-page-rating",
  ".nocontent",
  ".devsite-article-meta",
  ".devsite-floating-action-buttons",
];

// Zero-width, bidi-override, and tag-block characters have no business in
// vendored prose and are a prompt-injection smuggling vector.
const INVISIBLE_UNICODE =
  /[\u{200B}-\u{200F}\u{202A}-\u{202E}\u{2060}-\u{2064}\u{FEFF}\u{E0000}-\u{E007F}]/u;

function slugFor(url: string): string {
  const segments = new URL(url).pathname.split("/").filter(Boolean);
  return segments[segments.length - 1];
}

function extractUrls(indexMarkdown: string): string[] {
  const urls = [
    ...indexMarkdown.matchAll(/https:\/\/developers\.google\.com\/[\w\/-]+/g),
  ].map((m) => m[0]);
  return [...new Set(urls)];
}

function cleanArticle(html: string, url: string): HTMLElement {
  const root = parse(html);
  const article =
    root.querySelector("article.devsite-article") ??
    root.querySelector("article") ??
    root.querySelector("main");
  if (!article) throw new Error(`no <article> or <main> found in ${url}`);

  for (const selector of STRIP_SELECTORS) {
    for (const el of article.querySelectorAll(selector)) el.remove();
  }
  // Self-referencing anchor icons render as "[link](#term)" noise in Markdown.
  for (const a of article.querySelectorAll("a[aria-hidden]")) a.remove();
  for (const a of article.querySelectorAll("a")) {
    const href = a.getAttribute("href");
    if (href?.startsWith("/")) {
      a.setAttribute("href", `https://developers.google.com${href}`);
    }
  }
  return article;
}

function buildTurndown(): TurndownService {
  const turndown = new TurndownService({
    headingStyle: "atx",
    codeBlockStyle: "fenced",
    bulletListMarker: "-",
  });
  turndown.use(gfm);
  // The word list and several other pages are <dl> definition lists, which
  // turndown has no rule for; keep the term/guidance pairing explicit.
  turndown.addRule("definitionTerm", {
    filter: "dt",
    replacement: (content) => `\n\n**${content.trim()}**\n`,
  });
  turndown.addRule("definitionDescription", {
    filter: "dd",
    replacement: (content) => `\n${content.trim()}\n`,
  });
  return turndown;
}

function header(url: string, date: string): string {
  return [
    "<!--",
    `Source: ${url}`,
    `Snapshot: ${date}`,
    "License: CC BY 4.0 (page content), Apache 2.0 (code samples).",
    "Converted from HTML to Markdown; site navigation and boilerplate removed.",
    "See NOTICE.md in the repository root.",
    "-->",
    "",
  ].join("\n");
}

const dryRun = process.argv.includes("--dry-run");
const indexMarkdown = await readFile(indexPath, "utf8");
const urls = extractUrls(indexMarkdown);
if (urls.length === 0) throw new Error(`no URLs found in ${indexPath}`);

const slugs = urls.map(slugFor);
const collisions = slugs.filter((s, i) => slugs.indexOf(s) !== i);
if (collisions.length > 0) {
  throw new Error(`slug collisions: ${collisions.join(", ")}`);
}

if (dryRun) {
  for (const [i, url] of urls.entries()) {
    console.log(`${slugs[i].padEnd(28)} ${url}`);
  }
  console.log(`\n${urls.length} pages would be synced to ${outDir}`);
  process.exit(0);
}

await mkdir(outDir, { recursive: true });
const turndown = buildTurndown();
const date = new Date().toISOString().slice(0, 10);
const failures: string[] = [];

for (const [i, url] of urls.entries()) {
  const slug = slugs[i];
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const article = cleanArticle(await res.text(), url);
    const markdown = turndown
      .turndown(article.toString())
      .replace(/\n{3,}/g, "\n\n")
      .trim();

    if (markdown.length < MIN_CONTENT_CHARS) {
      throw new Error(`only ${markdown.length} chars of content`);
    }
    const invisible = markdown.match(INVISIBLE_UNICODE);
    if (invisible) {
      throw new Error(
        `invisible Unicode U+${invisible[0].codePointAt(0)!.toString(16)}`,
      );
    }

    await writeFile(join(outDir, `${slug}.md`), `${header(url, date)}\n${markdown}\n`);
    console.log(`ok   ${slug} (${markdown.length} chars)`);
  } catch (err) {
    failures.push(`${slug}: ${err instanceof Error ? err.message : err}`);
    console.error(`FAIL ${slug}: ${err}`);
  }
  if (i < urls.length - 1) await Bun.sleep(REQUEST_DELAY_MS);
}

if (failures.length > 0) {
  console.error(`\n${failures.length}/${urls.length} pages failed`);
  process.exit(1);
}
console.log(`\nSynced ${urls.length} pages to ${outDir}`);
