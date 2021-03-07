@echo off
rem =======================================================
rem プロジェクト情報
rem =======================================================

set UE4_VERSION=4.25
set UE4_DIR="D:\Program Files\Epic Games\UE_%UE4_VERSION%\Engine\Binaries\Win64"

set PROJECT_NAME=matching_hero
set RESOURCE_FOLDER_NAME=%PROJECT_NAME%_resources

set PROJECT_ROOT_DIR=%~dp0\..\..\
set UE4_PROJECT_DIR=%PROJECT_ROOT_DIR%\%PROJECT_NAME%\

set ASSET_DIR=D:\prog\0_myprogram\%RESOURCE_FOLDER_NAME%

set ASSET_MODEL_DIR=%ASSET_DIR%\models
set ASSET_CHARACTER_DIR=%ASSET_MODEL_DIR%\characters

set ASSET_OBJECT_DIR=%ASSET_MODEL_DIR%\objects

exit /b
