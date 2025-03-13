# Online Multiplayer FPS Game

## Overview
This is an **online multiplayer first-person shooter (FPS) game** built using **Unity** and the **Photon Framework**. The game features real-time multiplayer networking, a weapon and projectile system, and an interactive UI, providing an engaging FPS experience.

## Demo Video
https://github.com/tejas0230/Projects/assets/74281821/d405d4ae-5266-467b-9edb-c5f4dd97f869

## Features
- **Multiplayer Networking:** Player-hosted server architecture using **Photon PUN**, enabling real-time gameplay synchronization.
- **Weapon & Projectile System:** Includes bullet trajectory, impact detection, and damage calculation.
- **Character Controller:** Smooth player movement, input handling, and animation integration.
- **Matchmaking & Lobby:** Players can create/join rooms and compete in multiplayer matches.
- **Leaderboard & Stats:** Syncs player stats across sessions.
- **Game UI:** Includes HUD, menus, and in-game notifications.

## Technologies Used
- **Game Engine:** Unity
- **Networking:** Photon PUN (Photon Unity Networking)
- **Programming Language:** C#
- **Version Control:** Git & GitHub
- **UI Development:** Unity UI system

## Networking Details
- **Multiplayer Model:** Uses **Photon PUN** for client-server communication with a **player-hosted room system**.
- **Data Synchronization:** Player stats, animations, and game events are synchronized over the network.
- **Optimized RPC Calls:** Implemented **Remote Procedure Calls (RPCs)** to reduce unnecessary network traffic.
- **Matchmaking & Room Management:** Players can create or join lobbies using Photon’s matchmaking services.

## Setup & Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/tejas0230/FPS-Multiplayer.git
   ```
2. Run the "FPSMUltiplayer.exe" in the FPS_Build folder.

## Future Enhancements
- Add **dedicated server support** for better performance.
- Implement **customizable loadouts** for players.
- Introduce **voice chat** for in-game communication.
- Improve **AI bots** for offline practice mode.



