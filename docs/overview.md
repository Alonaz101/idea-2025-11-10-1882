# Project Overview

This project implements a Mood-Based Recipe Recommendation System, covering MVP and post-MVP features planned and described in Jira issues SCRUM-217 to SCRUM-222.

## Features Summary

### SCRUM-217: Mood Input Interface and Recipe Recommendation Engine (MVP)
- Frontend mood selection interface (simulated backend API provided here)
- Backend API for mood input and recipe matching logic

### SCRUM-218: User Profile and Preferences Management (MVP)
- APIs to get and update user preferences such as diet, allergies, and saved recipes

### SCRUM-219: Recipe Details, Saving & Sharing Features (MVP)
- Recipe detail APIs with ingredients, steps, and nutrition info
- APIs to save/bookmark recipes and share recipes on social media

### SCRUM-220: Machine Learning Based Recommendation Engine (Post-MVP)
- Stub implementation of an ML recommendation engine improving mood-to-recipe matching

### SCRUM-221: User Social Features (Comments, Sharing) (Post-MVP)
- APIs to comment on recipes and additional sharing functionality

### SCRUM-222: Mobile App and Voice-Based Mood Input (Future Expansion)
- Development roadmap includes mobile apps for iOS and Android
- Voice-based mood input accessibility features

---

## Backend Implementation Details
- Built with Flask
- In-memory data store for demos
- Modular with separate ML recommendation module
- Extendable for real database and ML model integration

## Repository Structure
- `backend/app.py`: Flask backend serving APIs
- `backend/ml_recommendation.py`: Stub ML recommendation module
- `docs/overview.md`: This project overview

This codebase represents a functional prototype aligning with the requirements outlined in the Jira issues, with traceability in commit messages referencing respective SCRUM tasks.