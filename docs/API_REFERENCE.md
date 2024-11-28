# API Reference

---

## Overview

This document outlines the available APIs, classes, and methods for interacting with Story Smith's core modules. It serves as a guide for developers looking to extend or integrate with the project.

---

## Module Overview

### `classes.py`

Manages character class definitions, stats, and abilities.

### Key Functions

- `load_classes(file_path: str) -> List[Dict]`
    
    Loads class definitions from `classes.json`.
    
- `modify_class_stat(class_name: str, stat: str, value: int) -> None`
    
    Dynamically modifies a class stat during gameplay.
    
- `apply_ability_effect(class_name: str, ability_name: str, target: Dict) -> None`
    
    Applies an ability's effect to a target.
    

---

### `ui.py`

Handles user interface components, including rendering and dynamic updates.

### Key Functions

- `initialize_ui() -> None`
    
    Initializes UI components and assets.
    
- `render_ui() -> None`
    
    Renders all UI elements to the screen.
    
- `update_ui(game_state: Dict) -> None`
    
    Updates the UI based on the current game state.
    

---

### `boss.py`

Manages boss interactions and multi-zone entities.

### Key Functions

- `initialize_boss(name: str) -> Dict`
    
    Creates a boss entity based on its name.
    
- `update_boss(boss: Dict, game_state: Dict) -> None`
    
    Updates the boss state based on the game state.
    

---

## Data Formats

### Example `classes.json`

```json
{
    "classes": [
        {
            "name": "Warrior",
            "attributes": {
                "health": 150,
                "strength": 20
            }
        }
    ]
}

```

## Example `boss.json`

```json
json
Copy code
{
    "bosses": [
        {
            "name": "Forest Guardian",
            "zones": [
                {"name": "Head", "health": 100}
            ]
        }
    ]
}

```

### **Next Steps**

1. **Generate Automatic Documentation**:
    - Use tools like `pydoc`, `sphinx`, or `mkdocs` to generate API references directly from docstrings in your code.
2. **Update as APIs Evolve**:
    - Ensure that this document is updated whenever new functions or modules are added.
3. **Link from Other Docs**:
    - Add references to the **API_REFERENCE.md** file in the **README.md** and other documentation files.
