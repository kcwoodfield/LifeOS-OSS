# Contributing to LifeOS-OSS

Thank you for your interest in contributing to LifeOS! This document explains how to contribute improvements back to the public template.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Workflow](#development-workflow)
4. [Branch Strategy](#branch-strategy)
5. [Contribution Guidelines](#contribution-guidelines)
6. [Privacy & Security](#privacy--security)
7. [Pull Request Process](#pull-request-process)

---

## Code of Conduct

Be respectful, constructive, and collaborative. We're building a tool to help people live better lives.

**Expected behavior:**
- Respectful communication
- Constructive feedback
- Focus on what's best for users
- Welcome newcomers

**Unacceptable:**
- Harassment or discrimination
- Trolling or inflammatory comments
- Sharing others' private information
- Unprofessional conduct

---

## How Can I Contribute?

### 1. Report Bugs

**Before submitting:**
- Check existing [GitHub Issues](https://github.com/kcwoodfield/LifeOS-OSS/issues)
- Verify it's not a configuration issue (check CLAUDE.md)
- Test with a fresh clone of the repo

**Bug report should include:**
- Clear, descriptive title
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots if relevant
- Environment (Obsidian version, Claude Code version, OS)

### 2. Suggest Enhancements

**Enhancement suggestions:**
- New agents or agent improvements
- New skills or skill enhancements
- Dashboard improvements
- Documentation improvements
- Workflow optimizations

**Proposal should include:**
- Clear use case (why is this needed?)
- How it fits into LifeOS philosophy
- Rough implementation approach
- Any breaking changes

### 3. Contribute Code

**Welcome contributions:**
- New agents (with complete documentation)
- New skills (following existing patterns)
- Dashboard templates
- Bug fixes
- Documentation improvements
- Example files

**See [Development Workflow](#development-workflow) below**

### 4. Improve Documentation

Documentation is crucial! Contributions welcome:
- Fix typos or unclear language
- Add examples or use cases
- Improve setup instructions
- Create tutorials or guides

---

## Development Workflow

### Initial Setup

1. **Fork the repository:**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/LifeOS-OSS.git
   cd LifeOS-OSS
   ```

2. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/kcwoodfield/LifeOS-OSS.git
   git fetch upstream
   ```

3. **Install development environment:**
   - Obsidian (latest version)
   - Claude Code (latest version)
   - Required plugins: Dataview, Templater

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make your changes:**
   - Follow existing code/documentation style
   - Test thoroughly in Obsidian
   - Add example files if needed
   - Update documentation

3. **Commit with clear messages:**
   ```bash
   git add -A
   git commit -m "Add [feature]: clear description

   - Detail 1
   - Detail 2

   Fixes #123"
   ```

4. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request:**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill out PR template (see below)

---

## Branch Strategy

LifeOS uses a **three-branch model** for privacy:

### Branches

**main** (private - not in LifeOS-OSS)
- Your personal data
- Never pushed to public repo
- Your daily driver

**workos** (private - not in LifeOS-OSS)
- Your work data
- Separate from personal
- Optional for users

**oss-template** (public - THIS REPO)
- Sanitized template
- No personal data
- What users clone

### Contributing to LifeOS-OSS

**You're contributing to `oss-template` branch** (the public template).

This branch contains:
- ✅ Infrastructure (agents, skills, schemas)
- ✅ Documentation (README, CLAUDE.md, etc.)
- ✅ Example files (example-*.md)
- ❌ Personal data (ignored by .gitignore)

---

## Contribution Guidelines

### Agents

**When creating a new agent:**

1. **File location:** `.system/agents/your-agent.md` or `.workos/agents/your-agent.md`

2. **Required sections:**
   - Role description
   - Expertise
   - Principles (decision-making framework)
   - When to consult
   - How agent works
   - Example consultations

3. **Style:**
   - Clear personality (but professional)
   - Specific expertise (not too broad)
   - Actionable advice (not generic)
   - Example-driven

4. **Documentation:**
   - Add to README.md agent list
   - Update CLAUDE.md if needed
   - Provide invocation examples

**Example PR:** "Add Recruiter agent to Growth division"

### Skills

**When creating a new skill:**

1. **File location:** `.claude/skills/your-skill/SKILL.md`

2. **Required elements:**
   - Clear trigger phrases
   - What the skill does
   - Output location
   - Step-by-step instructions
   - Example output
   - Integration with agents

3. **Testing:**
   - Test with example data
   - Test with empty databases
   - Verify output format
   - Check error handling

4. **Documentation:**
   - Add to README.md
   - Add to `.claude/skills/README.md`
   - Provide usage examples

**Example PR:** "Add habit tracking skill"

### Dashboards

**When creating a dashboard:**

1. **File location:** `dashboards/your-dashboard.md`

2. **Required:**
   - Clear purpose
   - Dataview queries (well-commented)
   - Works with example data
   - Mobile-friendly layout

3. **Best practices:**
   - Use Dataview, not DataviewJS (when possible)
   - Group related information
   - Add empty state messages
   - Keep queries performant

**Example PR:** "Add health tracking dashboard"

### Documentation

**When updating docs:**

- Use clear, simple language
- Include examples
- Test instructions (fresh clone)
- Update table of contents if needed
- Check all links work

---

## Privacy & Security

**CRITICAL: Never commit personal data**

### Before Submitting PR

1. **Review changes:**
   ```bash
   git diff origin/oss-template
   ```

2. **Check for personal info:**
   ```bash
   # Search for common personal data
   grep -r "YOUR_NAME" .
   grep -r "YOUR_EMAIL" .
   # Check context files
   cat .system/context/*.md
   cat .workos/context/*.md
   ```

3. **Verify .gitignore:**
   ```bash
   git status --ignored
   ```

4. **Only example data:**
   - Use `example-*.md` naming
   - Generic but realistic data
   - No real names, emails, companies

### What NOT to Commit

❌ Personal context files (`.system/context/*.md`)
❌ Real tasks, projects, or journal entries
❌ Real meeting notes or communications
❌ Personal photos or documents
❌ API keys, credentials, secrets

### What TO Commit

✅ Infrastructure (agents, skills, schemas)
✅ Example files (`example-*.md`)
✅ Templates (`.template` files)
✅ Documentation
✅ Bug fixes

---

## Pull Request Process

### PR Template

```markdown
## Description
[Clear description of what this PR does]

## Type of Change
- [ ] Bug fix
- [ ] New feature (agent, skill, dashboard)
- [ ] Documentation improvement
- [ ] Performance improvement
- [ ] Other (describe)

## Changes Made
- [List of specific changes]
- [Use bullets]

## Testing
- [ ] Tested in Obsidian
- [ ] Tested with Claude Code
- [ ] Works with example data
- [ ] No personal data included

## Screenshots (if applicable)
[Add screenshots of dashboards, skills output, etc.]

## Checklist
- [ ] Code follows existing style
- [ ] Documentation updated
- [ ] No personal data included
- [ ] Examples added if needed
- [ ] Tested thoroughly

## Related Issues
Fixes #[issue number]
```

### Review Process

1. **Automated checks:**
   - No personal data (checked manually)
   - Links valid
   - No broken references

2. **Manual review:**
   - Maintainer reviews code/docs
   - Suggests improvements
   - Approves or requests changes

3. **Merge:**
   - Squash and merge (clean history)
   - Delete feature branch
   - Close related issues

### After Merge

Your contribution is now part of LifeOS-OSS! 🎉

**Sync your fork:**
```bash
git checkout oss-template
git fetch upstream
git merge upstream/oss-template
git push origin oss-template
```

---

## Development Tips

### Testing Your Changes

**Fresh clone test:**
```bash
# Clone fresh
git clone https://github.com/YOUR_USERNAME/LifeOS-OSS.git test-install
cd test-install
git checkout your-branch-name

# Test in Obsidian
# Test skills in Claude Code
# Verify examples work
```

**Dataview query testing:**
- Use Dataview plugin's "Execute" button
- Check query against example files
- Verify empty state handling

**Skill testing:**
- Test with example data
- Test with empty databases
- Verify output paths correct
- Check error handling

### Style Guidelines

**Markdown:**
- Use headers appropriately (# → ## → ###)
- Lists for scannable content
- Code blocks with language tags
- Links to related content

**Frontmatter:**
- Follow existing schemas
- Use consistent date format (YYYY-MM-DD)
- Include all required fields
- Add helpful optional fields

**File naming:**
- Kebab-case: `my-file-name.md`
- Examples: `example-task-name.md`
- Dates: `YYYY-MM-DD-description.md`

---

## Questions?

**Need help?**
- Open an issue with `[Question]` tag
- Check existing discussions
- Review CLAUDE.md for system details

**Want to discuss major changes?**
- Open an issue first
- Describe your proposal
- Get feedback before coding

---

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Commit history (Co-Authored-By)

Thank you for making LifeOS better! 🙏

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
