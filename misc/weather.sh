#!/bin/bash
LANGUAGE="zh-CN"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

curl \
  -H "Accept-Language: $LANGUAGE" \
  -H "User-Agent: $UA" \
  'wttr.in/Shanghai?format=%l:+%c(%C)%20%t(feels:%20%f)%20%w%20%h%20%P%20%p%20%m\nSunrise:%09%S\nZenith:%09%z\nSunset:%09%s\nDusk:%09%d&m&M' -o $FILE_PATH
