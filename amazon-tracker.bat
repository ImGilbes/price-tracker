@echo OFF
cls
echo Running the tracker for Amazon prices (selected from the provided list)
echo This can take some time
python tracker.py amz
echo I'm now displayin the price changes
python analyzer.py amz
pause