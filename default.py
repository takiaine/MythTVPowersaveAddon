import xbmc
import subprocess

while (not xbmc.abortRequested):
	print "check new values"
	retVal = subprocess.check_output(["bash", "/home/antti/.xbmc/addons/MythTVPowersaveAddon/checkMythStatus.sh"])
	print retVal
	try:
		ret = int(retVal)
	except ValueError:
		ret = 1
	print ret
	it = xbmc.getGlobalIdleTime()
	print it
	if(it > 60*60 and ret == 0 and xbmc.getCondVisibility("System.ScreenSaverActive")):
		xbmc.executebuiltin('XBMC.Quit()')
		print "executebuiltin('XBMC.Quit()')"
	xbmc.sleep(60000)
