# Arch's arrows

**Currently on beta**

## Concept
The idea is to create a [website](http://yabirgb.com/arrows/) where to easily choose the one packages you like to install and don't worry about writing commands or looking for them or the packages. Also you can save your scripts and run them in different computers. It should be useful for  the situations where you have to install a large list of packages or when a package is difficult to get installed.

## How does it work?
It runs over a django app that has defined a models and runs a python script to sync database and github recipies folder(it uses a cron task). I have decided to use the this setup to avoid exceeds in the github's api ratelimits and to speed up the process.

## Support
You can help the project by adding recipes to the repository. The scheme is a json file with the name of the package, the library that it uses to install the package and the command used. Since the script ask for sudo privileges at the beginning is not needed to add "sudo" to the command.

```json
{
    "name": "FileZilla",
    "uses":["pacman"],
    "command":"pacman -S filezilla",
    "category": "Apps"
}
```

The category tag is tag to separate apps in the website. I suggest "Apps" for applications, "Themes" for themes, "Icons" for icons.
