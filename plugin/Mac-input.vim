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
if !exists('g:input_remote_timeout')
    let g:input_remote_timeout=0.5
endif

"echo g:input_zh
"echo g:input_en

if exists('$SSH_CONNECTION')
    let g:im_select_bin= expand('<sfile>:p:h') ."/remote/im_select_client.py"
    ":echo g:im_select_bin
elseif has('mac')
    let g:im_select_bin="im-select"
else
    finish
endif

function ImCmdList(im_select_bin, im, timeout)
    if has('mac')
        if a:im == ""
            return [a:im_select_bin]
        else
            return [a:im_select_bin, a:im]
        endif
    endif
    return [a:im_select_bin, a:im, a:timeout]
endfunction


"let result=trim(system(g:im_select_bin))
let result=trim(system(ImCmdList(g:im_select_bin, "", string(g:input_remote_timeout))))
if v:shell_error != 0
    echohl WarningMsg | echo result | echohl None
    finish
endif
if ! exists('result')
    finish
endif
let g:input_last = result

func Input2normal()
    let result=trim(system(g:im_select_bin))
    if v:shell_error != 0
        "echo result
        return
    endif
    let g:input_last = result
    if g:input_last == g:input_zh
        let result=trim(system(ImCmdList(g:im_select_bin, g:input_en, g:input_remote_timeout)))
    endif
    "echo g:input_last
endfunc

func Input2insert()
    if g:input_last == g:input_zh
        "echo "Set to" . g:input_last
        let result=trim(system(ImCmdList(g:im_select_bin, g:input_last, g:input_remote_timeout)))
        if v:shell_error != 0
            "echo result
            return
        endif
    endif
    "echo g:input_last
endfunc


if exists('##InsertLeavePre')
    au InsertLeavePre * call Input2normal()
else
    au InsertLeave * call Input2normal()
endif
au InsertEnter * call Input2insert()
au CmdlineLeave [/\?] call Input2normal()
au CmdlineEnter [/\?] call Input2insert()

