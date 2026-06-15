---
title: "Building observability into Notion's dead-letter queue"
url: "https://www.notion.com/blog/building-observability-into-notions-dead-letter-queue"
date: "2026-06-04"
author: "Maya Lekhi"
feed_url: "https://www.notion.com/blog"
---
Notion engineered the DLQ Explorer to provide engineers with a browser-based interface for inspecting and recovering failed background tasks without requiring direct AWS access. The tool leverages Athena and partition projection over existing S3 buckets to enable structured queries, reducing investigation time from approximately 20 minutes to under one minute while maintaining security controls and audit trails for task recovery operations.
