# Project Moon

Manage a Soviet moon colony and mine for resources to ensure survival. Balance resources, politics, and crew morale in a hostile lunar environment.

📘 [Back to roadmap](README.md)

## Project Overview

This RTS-style game puts players in charge of a Soviet lunar colony, where they must gather resources, expand the base, and ensure the survival of their cosmonauts.

## Game Features

- Unit selection and movement system
- Resource gathering and management
- Base building and expansion
- Crew management with morale system
- Cold War era Soviet space aesthetic

## Technical Structure

### Folder Organization
- `/scenes/units`: Unit-related scenes and scripts
- `/scenes/world`: World, camera, and game controller
- `/scenes/systems`: Core game systems (selection, movement)
- `/scenes/ui`: User interface elements

### Key Systems
- **Unit System**: Controls individual cosmonaut behavior and capabilities
- **Selection System**: Handles selecting single or multiple units
- **Movement System**: Manages unit movement with formation control
- **Camera System**: Controls the game view with boundary limits

## UI Design System

Our visual design follows the "KosmoStil" system - a fusion of Soviet constructivist design principles with lunar industrial aesthetics. This system governs all visual aspects of the game including:

- Color palette (Soviet reds, industrial grays, lunar dust tones)
- Typography (technical yet propagandistic)
- UI components (brutalist industrial panels)
- Iconography (space program symbolism)
- Environmental design (lunar surface + industrial base)

📘 [View the complete  style guide](styleguide.html)

## Development Status

This project is currently in early development, focusing on core gameplay systems like unit selection and movement.

## Getting Started

1. Clone the repository
2. Open the project in Godot 4.3
3. Open the main scene at `/scenes/world/GameWorld.tscn`
4. Press F5 to run the game

## Controls
- Left-click: Select units
- Shift + left-click: Add/remove units from selection
- Left-click + drag: Box select multiple units
- Right-click: Move selected units to target location