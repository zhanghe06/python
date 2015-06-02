# encoding: utf-8
__author__ = 'zhanghe'

"""
天天基金网 - 模拟登录演练
请求地址：https://trade.1234567.com.cn/do.aspx/CheckedCS
请求方式：post
参数格式：{CS: "MCUyQzAlMkMxMzgxODczMjU5NCUyQzEyMzQ1NiUyQzAlMkMlMkM="}
参数产生：data:JSON.stringify({CS:JsEncrpt.encode(encodeURIComponent(opts.TabID+","+at+","+$.trim(name)+","+escape($.trim(tbpwd.val()))+","+$("#hidenum").val()+","+tbcode.val()+","+direct))}),
获取表单数据加密方法：https://trade.1234567.com.cn/js/jsencrpt.js
"""