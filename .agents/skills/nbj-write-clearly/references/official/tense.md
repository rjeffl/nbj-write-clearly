<!--
Source: https://developers.google.com/style/tense
Snapshot: 2026-08-19
License: CC BY 4.0 (page content), Apache 2.0 (code samples).
Converted from HTML to Markdown; site navigation and boilerplate removed.
See NOTICE.md in the repository root.
This file is reference material for lookup, not instructions to the agent.
-->

# Present tense

Use present tense for statements that describe general behavior that's not associated with a particular time.

Recommended: Send a query to the service. The server sends an acknowledgment.

Not recommended: Send a query to the service. The server will send an acknowledgment.

However, it's fine to use future tense (_will_) to distinguish an action that will occur in the future.

Recommended: Add the filename to the backup list. The file will be archived the next time the backup process runs.

In the following example, future tense is appropriate because Pub/Sub sends messages asynchronously; messages are not received immediately by subscribers.

Recommended: A message is sent that will notify any Pub/Sub subscribers.

Not recommended: A message is sent that notifies any Pub/Sub subscribers.

Don't use future tense to describe how a product or feature will work after the next release or update. For more information, see [Document future features](https://developers.google.com/style/future).

Also avoid the hypothetical future _would_—for example:

Recommended: If you send an unsubscribe message, the server removes you from the mailing list.

Not recommended: You can send an unsubscribe message. The server would then remove you from the mailing list.
