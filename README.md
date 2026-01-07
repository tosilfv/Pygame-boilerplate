# Pygame Hotel Piccolo Game

## Video

![Video](video_1.gif)

## Description

This is a [Pygame](https://www.pygame.org/docs/) game.<br />
You control the piccolo that works in a hotel.<br />

## Background

Program is developed with [Cursor](https://cursor.com/) in Python.<br />
Install Cursor, python 3 and required libraries.<br />
Run main.py in the root folder to start the program.<br />
The game is created using the 
[Mediator Pattern](https://en.wikipedia.org/wiki/Mediator_pattern),<br />
where the Mediator is notified of any actions in the game by the game<br />
objects. Mediator then notifies the relevant game objects in return to<br />
react to these actions.<br />

## Testing

Install pytest: pip install -r requirements-dev.txt<br />
Run all tests with verbose output: pytest -v<br />

## Changelog

**[0.0.1] - Dec 12. 2025:**<br />
_- Initial Upload with original music and artwork._<br />

**[0.0.2] - Dec 13. 2025:**<br />
_- Refactored classes._<br />

**[0.0.3] - Dec 14. 2025:**<br />
_- Implemented the Mediator pattern._<br />

**[0.0.4] - Dec 30. 2025:**<br />
_- Implemented the background change._<br />
_- Added unit tests._<br />
_- Added documentation._<br />

**[0.0.5] - Dec 31. 2025:**<br />
_- Added graphics._<br />

**[0.0.6] - Jan 1. 2026:**<br />
_- Modified graphics._<br />
_- Added audio._<br />
_- Added front desk screen._<br />
_- Added elevator screens._<br />
_- Added floor screens._<br />
_- Added elevator user input prompt for selecting floor._<br />
_- Added corridor screens._<br />
_- Utilized large images._<br />

**[0.0.7] - Jan 2. 2026:**<br />
_- Added corridor 2 scene._<br />
