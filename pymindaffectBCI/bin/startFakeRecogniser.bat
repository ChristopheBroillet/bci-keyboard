cd %~dp0
setlocal enabledelayedexpansion
set batdir=%~dp0
cd %batdir%
cd ..\mindaffectBCI\hub

java -cp "FakeRecogniser.jar;UtopiaServer.jar" nl.ma.utopia.fakerecogniser.FakeRecogniser localhost:8400 1 1
