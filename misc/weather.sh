#!/bin/bash

curl 'wttr.in/Shanghai?format=%l:+%c(%C)%20%t(feels:%20%f)%20%w%20%h%20%P%20%p%20%m\nSunrise:%09%S\nZenith:%09%z\nSunset:%09%s\nDusk:%09%d&m&M' -o $FILE_PATH
