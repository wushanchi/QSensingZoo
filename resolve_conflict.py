#!/usr/bin/env python3
# Resolve the git merge conflict in README.md

with open('README.md', 'r') as f:
    lines = f.readlines()

# Find conflict markers
conflict_start = None
conflict_sep = None
conflict_end = None

for i, line in enumerate(lines):
    if line.startswith('<<<<<<<'):
        conflict_start = i
    elif line.startswith('======='):
        conflict_sep = i
    elif line.startswith('>>>>>>>'):
        conflict_end = i
        break

print(f"Conflict: start={conflict_start}, sep={conflict_sep}, end={conflict_end}")

# HEAD content (before separator)
# Lines 1-8: header (keep as is)
# Lines 9-103: content from HEAD (keep) - but skip the conflict markers at 9 and sep+1 to end
# After conflict: lines 106-...: content from origin/main

# Build the resolved content
# Lines 0-8 (header)
# Lines 10-103 (HEAD content before conflict)
# Lines 107 to conflict_end-1 (origin/main content after conflict marker, up to but not including "---...")
# Then continue with rest of origin/main

# First, let's find where origin/main's 20:03 section starts after the conflict
# We'll keep everything from line 137 onwards (20:03 section and older)
# But skip the 21:03 section from origin/main since we inserted it

# New section to insert: 21:03 entries from origin/main
new_section_lines = []
in_new_section = False
for i in range(conflict_sep + 1, conflict_end):
    line = lines[i]
    if line.startswith('>>>>>>>'):
        break
    if '### 🆕 新增条目(2026-08-03晚上-21:03' in line:
        in_new_section = True
    if in_new_section:
        new_section_lines.append(line)

# Find the 20:03 section start
# The "晚上-20:03" section starts after "*本次更新...21:03*" and "---"
# Let's find where it is after conflict_end
section_20_03_start = None
for i in range(conflict_end + 1, len(lines)):
    if '晚上-20:03' in lines[i]:
        section_20_03_start = i
        break

print(f"20:03 section starts at line {section_20_03_start}")

# Now build the resolved file
resolved = []

# Header (lines 0-8)
resolved.extend(lines[0:9])  # lines 1-9 (0-indexed: 0-8)

# HEAD content (lines 10 to sep-1) - the 20:33 section
resolved.extend(lines[10:conflict_sep])  # 20:33 section + 21:33 section

# Add the 21:03 section footer and separator
footer_20_33 = resolved[-1]  # The footer line for 21:33 section
resolved.append('\n')

# Now add a new section header for the 21:03 entries from origin/main
# We need to create a combined section that acknowledges both local and remote contributions
resolved.append('#### 清华大学+origin/main remote:多体动力学冻结磁场测量/Q-CTRL Boulder Opal持续更新/北方材料院金刚石量子传感/2026年8月3日(2026-08-03)\n')
resolved.append('- *以下条目来自origin/main remote合并 — 原origin/main在本地20:33/21:33条目之后的更新:*\n')

# Add the new section entries (from origin/main 21:03)
for line in new_section_lines:
    resolved.append(line)

# Skip origin/main's 20:03 section since it's older content
# Actually let's keep it since it has distinct content from 20:33

# Find the --- separator before 20:03
separator_20_03 = None
for i in range(section_20_03_start, len(lines)):
    if lines[i].strip() == '---':
        separator_20_03 = i
        break

# Add separator and 20:03 section
resolved.append('\n---\n\n')
resolved.append(lines[section_20_03_start:])  # rest of the file from 20:03 onwards

# Write the resolved content
with open('README.md', 'w') as f:
    f.writelines(resolved)

print(f"Resolved! Total lines: {len(resolved)}")
