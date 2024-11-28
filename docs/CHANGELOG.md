---

# **Changelog**

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## **[Unreleased]**

### Added

- Placeholder for ongoing changes and features being developed.

---

## **[1.0.0] - YYYY-MM-DD**

### Added

- Initial implementation of the `Narrative Engine` in `storyteller.py` for branching story paths.
- `classes.py` with dynamic loading from `classes.json` and stat management.
- `boss.py` to handle multi-zone boss encounters using data from `boss.json`.
- Base rendering functionality in `ui.py` for health gauges, menus, and overlays.
- Comprehensive unit tests for `classes.py`, `boss.py`, and `storyteller.py`.

### Changed

- Improved JSON schema for `classes.json` to include ability effects and metadata.
- Updated `README.md` with installation and usage instructions.

### Fixed

- Resolved an issue in `stage_manager.py` where layers were not rendering in the correct order.

---

## **[0.9.0] - YYYY-MM-DD**

### Added

- Prototype game loop in `main.py`.
- Placeholder assets in `assets/graphics` and `assets/sounds`.
- Initial folder structure for modular development.

---

## **How to Update the Changelog**

1. Use the **[Unreleased]** section to log ongoing changes during development.
2. When releasing a new version, create a new version section (e.g., **[1.1.0]**) and move the relevant changes from **[Unreleased]**.
3. Categorize changes under:
    - **Added**: For new features.
    - **Changed**: For updates to existing functionality.
    - **Fixed**: For bug fixes.
