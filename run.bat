@echo off
start /b python monit.py
start /b uvicorn main:app --reload