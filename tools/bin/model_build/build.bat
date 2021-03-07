@echo off
rem =======================================================
rem ���f���r���h
rem =======================================================

call %~dp0..\worktime.bat START

for /f "usebackq" %%A in (`time /t`) do set CURRENT_TIME=%%A
echo start time : %CURRENT_TIME%

call %~dp0..\project_def.bat

set NINJA_FILE_DIR=%~dp0ninja
set NINJA_CONFIG_DEST=%NINJA_FILE_DIR%\config.ninja
set NINJA_RULE_DEST=%NINJA_FILE_DIR%\rule.ninja
set NINJA_BUID_DEST=%NINJA_FILE_DIR%\build.ninja

python %~dp0scripts/ninja_model_config_writer.py --out %NINJA_CONFIG_DEST%
python %~dp0scripts/ninja_model_rule_writer.py --out %NINJA_RULE_DEST%
python %~dp0scripts/ninja_model_build_writer.py --out %NINJA_BUID_DEST%

rem ninja build�����s
rem   -j�̓X���b�h���A�X���b�h���𑝂₷�Ɓ@bpy.ops.object.parent_set(type='ARMATURE_AUTO') ��
rem   �������Ԃ�1���f��������5�����炢������悤�ɂȂ����̂ŃX���b�h����1�ɐݒ肵�Ă���B
%~dp0../../thirdparty/bin/ninja.exe -C %~dp0ninja -j 1 -v %*

call %~dp0..\worktime.bat STOP

for /f "usebackq" %%A in (`time /t`) do set CURRENT_TIME=%%A
echo All done. current=%CURRENT_TIME% elapsed=%DPS_STAMP%


pause
