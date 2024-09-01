@echo off
start /b uvicorn main:app --reload
start /b python monit.py