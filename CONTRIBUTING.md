# Contributing to FAIRy Lab

🎋 Thanks for your interest in FAIRy!

**FAIRy Lab** (this repo) is the UI + labs environment for FAIRy, built to make
it easy to run rulepacks, explore katas, and experiment with data validation
workflows on top of the FAIRy-core engine.

We welcome contributions from data stewards, curators, researchers, and
developers—especially around UX, labs/katas, and examples.

---

## Ways to contribute

There are many ways to help:

- **Use FAIRy Lab** and open issues for bugs, confusing behavior, or rough edges.
- **Improve the UI/UX**: workflows, layout, copy, accessibility, etc.
- **Add or refine labs / katas** (e.g. under `katas/`).
- **Improve documentation**: README, walkthroughs, screenshots, troubleshooting.
- **Add examples and demos** that show how FAIRy can be used in real workflows.

If you’re new, look for issues labeled `good first issue` or `help wanted`
in the issue tracker.

---

## Before you start

- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md).
- Make sure you have the tools listed in the project [README](./README.md)
  installed (for example Python / Streamlit / Node, depending on the setup).
- If you’re planning a **larger change** (new feature, major UI refactor),
  consider opening an issue first so we can discuss scope and approach.

---

## Development workflow

1. **Find or open an issue**

   - Check the [issue tracker](../../issues) for something interesting.
   - New contributors: start with `good first issue` or `help wanted`.
   - For new ideas, open an issue to discuss before you start coding.

2. **Fork and clone the repository**

   - Fork this repo on GitHub.
   - Clone your fork locally:

     ```bash
     git clone https://github.com/<your-username>/FAIRy-lab.git
     cd FAIRy-lab
     ```

3. **Create a feature branch**

   ```bash
   git switch -c feat/short-description

4. **Set up your environment**

   - Follow the setup instructions in the README
    (for example, creating a virtual environment and installing dependencies).
   - Make sure you can run the app locally (see the README for the command).

5. **Make your changes**

   - Keep changes focused and small where possible.
   - Update or add tests if the project includes them
   - Update documentation if behavior or UI changes.

6. **Run checks locally**

   - Run any linting / formatting tools described in the README.
   - Run tests if available (for example, pytest or other test commands).

7. **Submit a Pull Request**

   - Push your branc to your fork:
    ```bash
    git push -u origin feat/short-description
    ```
   - Open a Pull Request (PR) against the main branch of yuummmer/FAIRy-lab.
   - In the PR description, include:
        - a short summary of what you changed and why
        - a reference to the issue number (e.g. Fixes #42)
        - any notes for reviewers (breaking changes, screenshots, follow-ups, etc.)

We will review your PR as soon as we can. Friendly pings on status are welcome.
---

## Contributing labs, katas, and examples

FAIRy Lab is a great place to add small, focused “labs” that show FAIRy in action.
If you’d like to contribute a new kata or lab:

1. Open an issue describing:
- The dataset or domain you’re using.
- The goal of the lab (e.g. “validate a museum collection export”, “check ENA 
metadata for bulk submission”, “toy art collections example”).
- Any relevant standards or repositories (ENA, GEO, museum standards, etc.).

2. Create a new lab/kata directory (e.g. under katas/):
Include:
- A small sample dataset (or instructions on how to obtain it).
- A rulepack or configuration that FAIRy-core can run.
- A short README.md explaining:
    - What the lab is about.
    - How to run it (commands or UI steps).
    - What to look for in the results.

3. Keep datasets small and shareable
- Use synthetic or heavily downsampled data where possible.
- Avoid including sensitive or proprietary data.
---

## Issue labels

We use a few standard labels to help contributors find work:

- good first issue – Small, well-scoped tasks that are friendly to new contributors
- help wanted – We’d love community help; moderate difficulty
- docs – Documentation or examples
- ui / ux – User interface and experience improvements
- bug – Something is broken or not behaving as expected
- enhancement – New features or improvements

When you open a new issue, feel free to suggest labels; maintainers will adjust as needed.
---

## Licensing of contributions

By contributing to this repository, you agree that your contributions to the
application / UI code are licensed under the **MIT License** of this repo.
If you contribute example datasets or notebooks, we may mark those under
**CC BY-4.0** or similar open-science licenses so they can be reused with
attribution.
