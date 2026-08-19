<!--
Source: https://developers.google.com/style/placeholders
Snapshot: 2026-08-19
License: CC BY 4.0 (page content), Apache 2.0 (code samples).
Converted from HTML to Markdown; site navigation and boilerplate removed.
See NOTICE.md in the repository root.
-->

# Format placeholders

This page explains how to format placeholders in commands, code samples, and text strings. This page doesn't explain how to implement visual styling for placeholders, but it does show examples of how Google developer documentation style renders placeholders as visually distinct from other text.

For more information about formatting code, command-line syntax, and code samples, see the following links:

-   [Code in text](https://developers.google.com/style/code-in-text)
-   [Documenting command-line syntax](https://developers.google.com/style/code-syntax)
-   [Code samples](https://developers.google.com/style/code-samples)

Placeholders in sample code and commands represent values that the reader must replace when they use the sample input. Placeholders in example output can also represent other values that vary. In general, a placeholder has a descriptive name as a default value.

For example, the placeholder `PROJECT_ID` represents a project ID in sample code, commands, and example output.

In example output, the placeholder `HTTP_RESPONSE_CODE` represents an HTTP response code; the reader isn't expected to set this to a specific value.

## Placeholders

When you create placeholders follow this general guidance around using the letter _x_:

-   In general, don't use a single _x_ or a series of _x_'s as placeholders; use a more informative placeholder.
-   In some contexts (such as HTTP status codes), a series of _x_'s is the standard, so it's OK to use (for example) _xx_ in those cases.

There are several ways to format placeholders, depending on whether you're working in HTML or Markdown, or whether the placeholder is inline, in a code block, or in a paragraph. For details, see the following sections.

### Placeholders in inline text

If your sample code and command placeholders occur in a sentence, use the following formatting:

-   In HTML, wrap variable placeholders by using the `var` element, like this:
    
    <code><var>PLACEHOLDER\_NAME</var></code>
    
-   In Markdown, wrap inline placeholders in backticks (\`), and use an asterisk (\*) before the first backtick and after the second one (``*`PLACEHOLDER_NAME`*``).

If your placeholder does not represent a code sample or command, use the following formatting:

-   In HTML, wrap placeholders by using the `var` element, like this:
    
    <var>PLACEHOLDER\_NAME</var>
    

### Placeholders in code blocks

If your placeholders are in a block of code, use the following formatting:

-   In HTML, wrap the code block in a `pre` element, and tag placeholders with `var` elements:
    
          <pre>
          gcloud compute forwarding-rules create <var>FORWARDING\_RULE\_NAME</var> \\
              --global | --region=<var>REGION</var> \\
              --load-balancing-scheme=<var>LOAD\_BALANCING\_SCHEME</var> \\
              --network=<var>NETWORK</var> \\
              ...
          </pre>
          
-   In Markdown, wrap the code block in a code fence (\`\`\`). Inside a code fence, you can't apply formatting like bold or italic.
    
    \`\`\`
    PLACEHOLDER\_NAME
    \`\`\`
    

### Placeholder text

**Use uppercase characters with underscore delimiters.**

For example, in HTML:

Recommended:

-   `.../<var>API_NAME</var>`
-   `.../<var>METHOD_NAME</var>`

Not recommended:

-   `.../<var>API-name</var>`
-   `.../<var>API_name</var>`
-   `.../<var>API name</var>`
-   `.../<var>api_name</var>`
-   `.../<var>api-name</var>`
-   `.../<var>apiName</var>`

In Markdown:

Recommended:

-   `.../*API_NAME*`
-   `.../*METHOD_NAME*`

If the context in which your placeholders appear makes using uppercase characters with underscore delimiters a bad idea, use something else that makes sense to you, but be internally consistent.

**Don't include possessive adjectives in placeholders.**

Not recommended:

-   `.../<var>MY_API_NAME</var>`
-   `.../<var>YOUR_API_NAME</var>`

**Note**: You can mark up command-line syntax with [brackets](https://developers.google.com/style/code-syntax#optional-arguments), [braces](https://developers.google.com/style/code-syntax#set-of-two-arguments), and [ellipses](https://developers.google.com/style/code-syntax#arguments-that-can-repeat). Don't put the brackets, braces, or ellipses in the `var` element.

## Explain placeholders

When you use a placeholder in text or code, explain the placeholder the first time you use it. It's not necessary to repeat the explanation in the document unless doing so might benefit the reader—for example, in circumstances such as the following:

-   Your document is lengthy.
-   You've introduced several other placeholders in a long procedure.
-   Your document isn't intended to be read from beginning to end.

The following is an example of a command that uses a placeholder with an explanation of that placeholder:

<pre class="devsite-click-to-copy">
gcloud compute instances create <var>INSTANCE\_NAME</var> \\
    --metadata enable-guest-attributes=TRUE
</pre>

<p>Replace <code><var>INSTANCE\_NAME</var></code> with the name that
you want your new VM instance to have.</p>

### Single placeholder

Use the following format for a single placeholder:

-   Replace PLACEHOLDER with a description of what the placeholder represents.

Recommended:

1.  Stream the build logs to the Google Cloud console:
    
    gcloud builds log --stream=BUILD\_ID
    
    Replace `BUILD_ID` with the ID of the `WORKING` build that you copied in the preceding step.
    

### Two or more placeholders

Use the following format for two or more placeholders:

-   Follow the command line with a descriptive list of the placeholders used in the command line. Explain what each placeholder represents even if the placeholder value is intuitive to you.
-   Introduce this list with _Replace the following:_
-   List the placeholders in the order in which they appear in the command line.
-   Tag each placeholder in a code sample or command with `code` and `var` elements, followed by a [colon and a description that starts with a lowercase letter](https://developers.google.com/style/colons). For non-code samples, remove the `code` elements—for example:
    
    <li><code><var>INSTANCE\_NAME</var></code>: description</li>
    
-   If the description contains an example, introduce it with an _em dash_ or _such as_—for example:
    
    <li><code><var>INSTANCE\_NAME</var></code>: description&mdash;for example,...</li>
    
    <li><code><var>INSTANCE\_NAME</var></code>: description, such as...</li>
    
-   Each item in the list follows our [list style](https://developers.google.com/style/lists).

Recommended:

1.  Set the maximum concurrency target for a new reservation:
    
        bq mk \\
            --project\_id=ADMIN\_PROJECT\_ID \\
            --location=LOCATION \\
            --target\_job\_concurrency=CONCURRENCY \\
            --reservation \\
            RESERVATION\_NAME
    
    Replace the following:
    
    -   `ADMIN_PROJECT_ID`: the project that owns the reservation
    -   `LOCATION`: the location of the reservation
    -   `CONCURRENCY`: the maximum concurrency target
    -   `RESERVATION_NAME`: the name of the reservation

Recommended:

1.  In Cloud Shell, set the environment variables:
    
    export ONPREM\_PROJECT=ON\_PREM\_PROJECT\_NAME \\
        export ONPREM\_ZONE=ZONE
    
    Replace the following:
    
    -   `ON_PREM_PROJECT_NAME`: the Google Cloud project name for your on-premises project. You can find your project number on the [Dashboard](https://console.cloud.google.com/home/dashboard) page of the Google Cloud console.
    -   `ZONE`: a [Google Cloud zone](https://developers.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) that's close to your location—for example, `us-east1`.

### Placeholders in output

If you provide a code output example, explain any placeholders that appear in sample output:

-   Use `var` elements to identify the placeholder text in the output.
-   Follow the example output with a list of the placeholders used in the example.
-   Introduce the list of placeholders with _This output includes the following values:_
-   List the placeholders in the order in which they appear in the example.
-   Tag each placeholder with a `var` element, followed by a colon and a description that starts with a lowercase letter—for example:
    
    <li><code><var>INSTANCE\_NAME</var></code>: description</li>
    
-   If the description contains an example, introduce it with an _em dash_ or _such as_—for example:
    
    <li><code><var>INSTANCE\_NAME</var></code>: description&mdash;for example,...</li>
    
    <li><code><var>INSTANCE\_NAME</var></code>: description, such as...</li>
    

For more information, see [Output from commands](https://developers.google.com/style/code-syntax#output).

Recommended:

#### Response

The output is similar to the following:

{
 "name": "operations/build/PROJECT\_ID/OPERATION\_ID",
 "metadata": {
  "@type": "type.googleapis.com/google.devtools.cloudbuild.v1.BuildOperationMetadata",
  "build": {
   "id": "BUILD\_ID",
   "status": "QUEUED",
   "createTime": "2019-09-20T15:55:29.353258929Z",
   "steps": \[
    {
     "name": "gcr.io/compute-image-import/gce\_vm\_image\_import:release",
     "env": \[
      "BUILD\_ID=BUILD\_ID"
     \],
     "args": \[
      "-timeout=7056s",
      "-image\_name=IMAGE\_NAME",
      "-client\_id=api",
      "-data-disk",
      "-source\_file=SOURCE\_FILE"
     \]
    }
   \],
   "timeout": "7200s",
   "projectId": "PROJECT\_ID",
   "logsBucket": "gs://PROJECT\_NUMBER.cloudbuild-logs.googleusercontent.com",
   "options": {
    "logging": "LEGACY"
   },
   "logUrl": "https://console.cloud.google.com/gcr/builds/BUILD\_ID?project=PROJECT\_NUMBER"
  }
 }
}

This output includes the following values:

-   `PROJECT_ID`: the project ID for the project that the image was imported into
-   `OPERATION_ID`: the ID of the import operation
-   `BUILD_ID`: the ID of the build for the import operation
-   `IMAGE_NAME`: the name of the image to be imported
-   `SOURCE_FILE`: the URI for the image in Cloud Storage—for example, `gs://my-bucket/my-image.vmdk`
-   `PROJECT_NUMBER`: the number for the import project
