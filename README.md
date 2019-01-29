# oiio-python

OpenImageIO Python 3.x package.

| Build pipeline | R&D Status | CI Status |
| ------------- | ------------- | ------------- |
| win2016 | Wheels are building | [![Build Status](https://fredrikaverpil.visualstudio.com/oiio-python/_apis/build/status/oiio-python-win2016?branchName=master)](https://fredrikaverpil.visualstudio.com/oiio-python/_build/latest?definitionId=5?branchName=master) |
| ubuntu 16.04 | Solving issues | [![Build Status](https://fredrikaverpil.visualstudio.com/oiio-python/_apis/build/status/oiio-python-ubuntu16.04?branchName=master)](https://fredrikaverpil.visualstudio.com/oiio-python/_build/latest?definitionId=6?branchName=master) |
| macOS | Not started | |

## About the project

We are attempting to build oiio for Python 3.x (wheels) using [vcpkg]() on Windows, Linux and macOS.

## Download wheels

Since the project is still in a r&d phase, no releases have been made just yet. Instead, look at the CI builds where wheels are stored as build artifacts after successful builds.

For each Azure Pipelines build, click the "Summary" link, and you will see the build artifacts (Python wheels).

## Notes

- Official oiio repository at [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio), note the `.travis.yml` and `appveyor.yml`
- The python3 files for oiio at [vcpkg/ports/python3](https://github.com/Microsoft/vcpkg/tree/master/ports/python3)
- The vcpkg files for oiio at [vcpkg/ports/openimageio](https://github.com/Microsoft/vcpkg/tree/master/ports/openimageio)
