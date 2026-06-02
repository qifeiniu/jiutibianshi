#!/usr/bin/env python3
"""Generate three separate phone mockups for each tab state."""
import re

with open('btm.html', 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')

# Extract the shared header part (lines 217-290, phone shell + status bar + profile + notification)
# Line numbers are 1-indexed in the file, 0-indexed in array
header_lines = lines[216:290]  # lines 217-290
header = '\n'.join(header_lines)

# Extract tab contents
# Tab basic content: lines 311-400 (the div with id=tab-basic, inner content)
tab_basic_lines = lines[310:400]
tab_basic = '\n'.join(tab_basic_lines)

# Tab body content: lines 403-498
tab_body_lines = lines[402:498]
tab_body = '\n'.join(tab_body_lines)

# Tab special content: lines 501-580
tab_special_lines = lines[500:580]
tab_special = '\n'.join(tab_special_lines)

# Quick entry + bottom bar: lines 583-607
footer_lines = lines[582:607]
footer = '\n'.join(footer_lines)

def make_phone(tab_name, tab_label, tab_basic_content, tab_body_content, tab_special_content, active_tab, subtitle):
    """Create a phone mockup with a specific tab active."""
    # Tab bar with active state
    tabs_html = '''        <!-- Tab Bar -->
        <div class="mx-5 mb-3">
          <div class="flex items-center justify-between bg-white rounded-t-2xl px-2 pt-3 pb-0">
            <button class="flex-1 flex flex-col items-center gap-1.5 pb-2 relative">
              <span class="text-[15px] {basic_style}">基础指标</span>
              <div class="w-5 h-[3px] rounded-full {basic_indicator}"></div>
            </button>
            <button class="flex-1 flex flex-col items-center gap-1.5 pb-2 relative">
              <span class="text-[15px] {body_style}">体成分指标</span>
              <div class="w-5 h-[3px] rounded-full {body_indicator}"></div>
            </button>
            <button class="flex-1 flex flex-col items-center gap-1.5 pb-2 relative">
              <span class="text-[15px] {special_style}">专项指标</span>
              <div class="w-5 h-[3px] rounded-full {special_indicator}"></div>
            </button>
          </div>'''

    active_s = 'font-bold text-gray-900'
    inactive_s = 'font-normal text-gray-400'
    active_i = 'bg-blue-500'
    inactive_i = 'bg-transparent'

    tabs_html = tabs_html.format(
        basic_style=active_s if active_tab == 'basic' else inactive_s,
        basic_indicator=active_i if active_tab == 'basic' else inactive_i,
        body_style=active_s if active_tab == 'body' else inactive_s,
        body_indicator=active_i if active_tab == 'body' else inactive_i,
        special_style=active_s if active_tab == 'special' else inactive_s,
        special_indicator=active_i if active_tab == 'special' else inactive_i,
    )

    # Select the right content
    if active_tab == 'basic':
        content_html = tab_basic_content.replace('id="tab-basic" class="home-tab-content ', 'class="')
    elif active_tab == 'body':
        content_html = tab_body_content.replace('id="tab-body" class="home-tab-content ', 'class="').replace(' hidden', '')
    else:
        content_html = tab_special_content.replace('id="tab-special" class="home-tab-content ', 'class="').replace(' hidden', '')

    return f'''    <!-- {subtitle} -->
    <div class="flex flex-col items-center">
      <div class="w-[375px] h-[812px] bg-gray-50 rounded-[3rem] shadow-2xl overflow-hidden relative border-[8px] border-gray-800">
        <div class="absolute top-0 left-0 right-0 h-[380px] bg-gradient-to-b from-blue-400 via-blue-300 to-blue-100/30 pointer-events-none" style="z-index:0;"></div>
        <div class="relative" style="z-index:1;">
        <div class="flex justify-between items-center px-8 pt-3 text-white text-xs font-medium">
          <span>15:39</span>
          <div class="flex items-center gap-1"><i class="fa-solid fa-signal"></i><span class="text-[10px]">5G</span><i class="fa-solid fa-battery-three-quarters"></i></div>
        </div>
        <!-- App Name + Mini Program Capsule -->
        <div class="flex items-center justify-between px-5 pt-3 pb-2">
          <div class="flex items-center gap-2">
            <div class="w-8 h-8 bg-white/25 rounded-lg flex items-center justify-center backdrop-blur-sm">
              <i class="fa-solid fa-heartbeat text-white text-base"></i>
            </div>
            <h1 class="text-lg font-bold text-white" style="text-shadow: 0 1px 4px rgba(0,0,0,0.2); letter-spacing: 0.05em;">健康九体辨识</h1>
          </div>
          <div class="flex items-center h-[32px] bg-black/15 backdrop-blur-sm rounded-full border border-white/30" style="padding: 0 2px;">
            <button class="w-[34px] h-[28px] flex items-center justify-center">
              <svg width="18" height="4" viewBox="0 0 18 4" fill="none"><circle cx="2" cy="2" r="1.8" fill="white" opacity="0.9"/><circle cx="9" cy="2" r="1.8" fill="white" opacity="0.9"/><circle cx="16" cy="2" r="1.8" fill="white" opacity="0.9"/></svg>
            </button>
            <div class="w-px h-[18px] bg-white/30"></div>
            <button class="w-[34px] h-[28px] flex items-center justify-center">
              <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><line x1="2.5" y1="2.5" x2="9.5" y2="9.5" stroke="white" stroke-width="1.6" stroke-linecap="round" opacity="0.9"/><line x1="9.5" y1="2.5" x2="2.5" y2="9.5" stroke="white" stroke-width="1.6" stroke-linecap="round" opacity="0.9"/></svg>
            </button>
          </div>
        </div>
        <!-- Profile Info -->
        <div class="mx-5 relative overflow-visible mb-2" style="min-height:180px;">
          <div class="pt-4 pb-2 pr-[140px]">
            <div class="flex items-center gap-2 mb-2">
              <span class="text-2xl font-bold text-gray-900">本人</span>
              <i class="fa-solid fa-pen-to-square text-gray-500 text-sm cursor-pointer"></i>
            </div>
            <p class="text-sm text-gray-600 mb-2">男  45岁</p>
            <div class="flex items-center gap-2 mb-4">
              <span class="text-sm text-gray-600">BMI <i class="fa-solid fa-circle-question text-gray-400 text-[10px]"></i>：</span>
              <span class="text-base font-bold text-gray-900">24.8</span>
              <span class="bg-green-100 text-green-600 text-[10px] px-1.5 py-0.5 rounded font-medium">正常</span>
            </div>
            <div class="bg-white/60 backdrop-blur-sm rounded-xl px-3 py-2.5 flex items-start gap-2">
              <div class="w-6 h-6 bg-orange-400 rounded-full flex items-center justify-center shrink-0 mt-0.5">
                <i class="fa-solid fa-triangle-exclamation text-white text-[10px]"></i>
              </div>
              <div class="flex-1">
                <p class="text-sm font-bold text-gray-800 leading-tight">健康问题 <span class="text-orange-500">1</span> 项</p>
                <p class="text-xs text-gray-500 mt-0.5 flex items-center gap-0.5">查看健康计划 <i class="fa-solid fa-chevron-right text-[8px] text-gray-400"></i></p>
              </div>
            </div>
          </div>
          <div class="absolute right-0" style="bottom:-30px; width:160px; height:210px; pointer-events:none; z-index:0;">
            <img src="卡通医生.png" alt="卡通医生" class="w-full h-full object-contain object-bottom" style="filter: drop-shadow(0 4px 16px rgba(0,0,0,0.1));">
          </div>
        </div>

        <!-- Notification Card -->
        <div class="mx-5 bg-white rounded-2xl shadow-sm p-4 mb-3 flex items-center gap-3 relative" style="z-index:2;">
          <div class="relative shrink-0">
            <div class="w-11 h-11 bg-blue-50 rounded-xl flex items-center justify-center">
              <i class="fa-solid fa-file-medical text-blue-500 text-lg"></i>
            </div>
            <div class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center">
              <span class="text-white text-[8px] font-bold">1</span>
            </div>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm text-gray-800 font-semibold">您有一份新的健康报告</p>
            <p class="text-xs text-gray-400">2026-03-28 健康体检报告已生成</p>
          </div>
          <i class="fa-solid fa-chevron-right text-gray-300 text-xs shrink-0"></i>
        </div>

{tabs_html}

          <!-- Tab Content -->
{content_html}
        </div>

        <!-- Quick Entry -->
        <div class="mx-5 grid grid-cols-3 gap-3 pb-20">
          <div class="bg-white rounded-xl p-3 shadow-sm text-center">
            <div class="w-10 h-10 mx-auto bg-blue-50 rounded-full flex items-center justify-center mb-1"><i class="fa-solid fa-weight-scale text-blue-500"></i></div>
            <p class="text-xs text-gray-600">体脂数据</p>
          </div>
          <div class="bg-white rounded-xl p-3 shadow-sm text-center">
            <div class="w-10 h-10 mx-auto bg-purple-50 rounded-full flex items-center justify-center mb-1"><i class="fa-solid fa-yin-yang text-purple-500"></i></div>
            <p class="text-xs text-gray-600">体质辨识</p>
          </div>
          <div class="bg-white rounded-xl p-3 shadow-sm text-center">
            <div class="w-10 h-10 mx-auto bg-green-50 rounded-full flex items-center justify-center mb-1"><i class="fa-solid fa-file-medical text-green-500"></i></div>
            <p class="text-xs text-gray-600">健康报告</p>
          </div>
        </div>
        </div>
        <!-- Bottom Tab Bar -->
        <div class="absolute bottom-0 left-0 right-0 bg-white border-t border-gray-100 px-4 pb-6 pt-2" style="z-index:10;">
          <div class="flex justify-around">
            <div class="flex flex-col items-center gap-0.5"><i class="fa-solid fa-house text-blue-500 text-lg"></i><span class="text-[10px] text-blue-500 font-medium">首页</span></div>
            <div class="flex flex-col items-center gap-0.5"><i class="fa-solid fa-clipboard-list text-gray-400 text-lg"></i><span class="text-[10px] text-gray-400">记录</span></div>
            <div class="flex flex-col items-center gap-0.5"><i class="fa-solid fa-stethoscope text-gray-400 text-lg"></i><span class="text-[10px] text-gray-400">辨识</span></div>
            <div class="flex flex-col items-center gap-0.5"><i class="fa-solid fa-user text-gray-400 text-lg"></i><span class="text-[10px] text-gray-400">我的</span></div>
          </div>
        </div>
      </div>
      <p class="mt-3 text-sm font-medium text-gray-600">{subtitle}</p>
    </div>'''


# Generate three phone mockups
phone1 = make_phone('basic', '基础指标', tab_basic, tab_body, tab_special, 'basic', '2.1 健康档案 — 基础指标')
phone2 = make_phone('body', '体成分指标', tab_basic, tab_body, tab_special, 'body', '2.2 健康档案 — 体成分指标')
phone3 = make_phone('special', '专项指标', tab_basic, tab_body, tab_special, 'special', '2.3 健康档案 — 专项指标')

three_phones = phone1 + '\n\n' + phone2 + '\n\n' + phone3

# Find the original single phone block (lines 215-610) and replace it
# Line 215 (0-indexed: 214) starts with "    <!-- 2.1 首页（默认态） -->"
# Line 610 (0-indexed: 609) ends with "    </div>"
before = '\n'.join(lines[:214])  # lines 1-214
after = '\n'.join(lines[610:])   # lines 611 onwards

# Also update the empty state label from 2.2 to 2.4
after = after.replace('2.2 健康档案（空态 - 无数据）', '2.4 健康档案（空态 - 无数据）')

new_content = before + '\n' + three_phones + '\n\n' + after

with open('btm.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! Replaced single phone with 3 tab-state phones.")
