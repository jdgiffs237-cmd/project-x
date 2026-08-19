# 🛩️ The blog is here

**https://jdgiffs237-cmd.github.io/project-x/**

That's the live public build log. Bookmark it, or come back to this file.

| | |
|---|---|
| **Live site** | https://jdgiffs237-cmd.github.io/project-x/ |
| **About page** | https://jdgiffs237-cmd.github.io/project-x/about/ |
| **Contact page** | https://jdgiffs237-cmd.github.io/project-x/contact/ |
| **RSS feed** | https://jdgiffs237-cmd.github.io/project-x/feed.xml |
| **Repo** | https://github.com/jdgiffs237-cmd/project-x |
| **Deploy runs** | https://github.com/jdgiffs237-cmd/project-x/actions |

## How it gets published

The site source lives in [blog/](blog/). Push anything under `blog/` to `main`
and the [pages workflow](.github/workflows/pages.yml) rebuilds and deploys it —
usually live within a couple of minutes. There is no manual publish step.

To write a new entry, see [blog/README.md](blog/README.md).

## Comments

Readers can comment on any post — **no account needed**, they just type a name.
Comments are powered by [Cusdis](https://cusdis.com) and are **held for approval**:
nothing appears publicly until you approve it.

| | |
|---|---|
| **Moderate comments** | https://cusdis.com/dashboard |

### Switching them on (one-time, ~3 minutes)

Comments are wired up but dormant until you do this:

1. Sign up at **https://cusdis.com** (free tier is fine).
2. Create a website in the dashboard. Name it `Project X`, URL
   `https://jdgiffs237-cmd.github.io/project-x/`.
3. Copy the **App ID** it gives you (a long uuid).
4. Paste it into [blog/_config.yml](blog/_config.yml):

   ```yaml
   cusdis:
     app_id: "paste-the-uuid-here"
   ```

5. Commit and push. The comment box appears on every post within a couple of
   minutes.

Until step 4 is done, the comments section shows a line pointing readers at the
contact page instead — nothing looks broken.

**Turn on email notifications** in the Cusdis dashboard, or you won't know a
comment is waiting for approval.

## Contact shown on the site

Both are on the contact page and in the footer of every page:

- **Email:** joshuagifford237@gmail.com
- **Phone / text:** 610-389-5374

They come from the `contact:` block in [blog/_config.yml](blog/_config.yml) —
change them there and every page updates. Deleting the `phone` lines removes
the phone from the site without any other edit.

---

*This file exists so the link is never something you have to go looking for.
Everything else about the project starts at [README.md](README.md).*
