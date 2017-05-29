@echo off
REM Launch script for Emiko
REM (c) CutePikachu / MiteBCool Technology LLC
REM We taskkill python to stop it multi-instancing, we don't need sharding atm
taskkill /f /im python.exe
python emiko.py