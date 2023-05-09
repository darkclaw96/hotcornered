# hotcornered
Python script to implement hot corners

Config file should be located at 
>$HOME/.config/hotcornered.ini

Features:
- Timeouts can be set for each corner
- Multi-monitor support
- Individual hot corners for separate monitors

Each separate monitor needs a separate section in the config:
>[monitor_name]
> ;; monitor name can be found using *xrandr*
> ;; resolution of the display
>width = 1920
>height = 1080
>hot_corner_size = 0.01 # percentage of the resolution
> ;; Top-left corner
>tl_command = "polybar-msg cmd toggle" 
>tl_timeout = 500
> ;; Top-right corner
>tr_command = "echo 'Hot corner undefined' | yad --text-info --close-on-unfocus"
>tr_timeout = 500
> ;; Bottom-left corner
>bl_command = "echo 'Hot corner undefined' | yad --text-info --close-on-unfocus"
>bl_timeout = 500
> ;; Bottom-right corner
>br_command = "echo 'Hot corner undefined' | yad --text-info --close-on-unfocus"
>br_timeout = 500
