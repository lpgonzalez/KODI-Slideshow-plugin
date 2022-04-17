import xbmc
import xbmcaddon


# entry point
if (__name__ == '__main__'):
    addonSettings = xbmcaddon.Addon(id='script.slideshow')
    slideshow_path = addonSettings.getSetting('slideshow_path')
    slideshow_random = addonSettings.getSetting('slideshow_random').lower() == 'true'

    if slideshow_random:
        xbmc.executebuiltin('SlideShow(' + slideshow_path + ',recursive, random)')
    else:
        xbmc.executebuiltin('SlideShow(' + slideshow_path + ',recursive, notrandom)')
