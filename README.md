Keep and restore Mac input method state for each buffer separately when leaving/re-entering insert mode or search mode. Like always typing English in normal mode, but Chinese in insert mode.

Inspired by lilydjwg's [fcitx.vim](https://github.com/lilydjwg/fcitx.vim). Implement through [im-select](https://github.com/daipeihust/im-select)

Requires:

* [im-select](https://github.com/daipeihust/im-select)

Configuration:

Get the name of input by `im-select`, in different mode of input method. Default input method of English is `'com.apple.keylayout.ABC'` and that of Chinese is `'com.apple.inputmethod.SCIM.ITABC'`. If you other keyboard layout, modify the following line and add to you vim configuration file.

```vim
# default input method of English in normal mode
let g:input_en='com.apple.keylayout.ABC'
# default input method of Chinese in insert mode
let g:input_zh='com.apple.inputmethod.SCIM.ITABC'
```

Warning:

1. If you use Vim in terminal, to avoid the Esc delay, please set `'ttimeoutlen'` to 100 or some other value. And check screen's `maptimeout` or tmux's `escape-time` option if you use it too.
2. There will be a delay when exiting from insert mode. During this delay time, if you input something, these inputs will stay in insert mode, and they need to be output after pressing the space in insert mode. So to avoid this, you need to wait for a while after pressing Esc.

Relative links:

* [vim-im-select](https://github.com/brglng/vim-im-select): Another plug-in that implements this function.



在离开或重新进入插入模式或搜索模式时自动记录和恢复每个缓冲区各自的输入法状态，以便在普通模式下始终是英文输入模式，切换回插入模式时恢复离开前的输入法输入模式。

受依云的[fcitx.vim](https://github.com/lilydjwg/fcitx.vim)的启发，通过[im-select](https://github.com/daipeihust/im-select)实现切换输入法。


要求:

* [im-select](https://github.com/daipeihust/im-select)


配置：

在不同的输入法模式下，通过`im-select`获取输入法的名称。 默认的英文输入法是`'com.apple.keylayout.ABC'`，默认的中文输入法是`'com.apple.inputmethod.SCIM .ITABC'`。 如果您使用其他键盘布局，请修改以下行并将其添加到您的 vim 配置文件中。

```vim
# default input method of English in normal mode
let g:input_en='com.apple.keylayout.ABC'
# default input method of Chinese in insert mode
let g:input_zh='com.apple.inputmethod.SCIM.ITABC'
```

注意事项:

1. 终端下请设置 Vim `'ttimeoutlen'` 选项为较小值（如100），否则退出插入模式时会有较严重的延迟。同样会造成延迟的还有 screen 的 `maptimeout` 选项以及 tmux 的 `escape-time` 选项。
2. 从插入模式退出时会有一段时间的延迟。 在这段延迟时间内，如果你输入了什么，这些输入会滞留在插入模式，这些错误的输入需要在插入模式下按空格后输出。 所以为了避免出现这种情况，你需要在按 Esc 后等待一段时间。

相关链接：

* [vim-im-select](https://github.com/brglng/vim-im-select)： 另一个实现此功能的插件。
