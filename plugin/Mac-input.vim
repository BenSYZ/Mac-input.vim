scriptencoding utf-8
" fcitx.vim	remember Mac-input's input state for each buffer
" Author:       BenSYZ
" Version:	1.1
" ---------------------------------------------------------------------

if ! exists('g:input_en')
    let g:input_en='com.apple.keylayout.ABC'
endif
if ! exists('g:input_zh')
    let g:input_zh='com.apple.inputmethod.SCIM.ITABC'
endif

let g:input_en=g:input_en . "\n"
let g:input_zh=g:input_zh . "\n"
"echo g:input_zh
"echo g:input_en


:let g:input_now=system('im-select')

if ! exists('input_last')
    :let g:input_last=g:input_now
endif
func Input2normal()
    :let g:input_now=system('im-select')
    if g:input_now == g:input_en
	let g:input_last = g:input_en
    elseif g:input_now == g:input_zh
	let g:input_last = g:input_zh
	:let status=system("im-select " . g:input_en)
    endif
    "echo g:input_now
endfunc

func Input2insert()
    "if g:input_last == g:input_en
    "    let g:input_last = g:input_en
    if g:input_last == g:input_zh
	:let status=system("im-select " . g:input_zh)
    endif
    "echo g:input_now
endfunc


if exists('##InsertLeavePre')
    au InsertLeavePre * call Input2normal()
else
    au InsertLeave * call Input2normal()
endif
au InsertEnter * call Input2insert()
au CmdlineLeave [/\?] call Input2normal()
au CmdlineEnter [/\?] call Input2insert()

