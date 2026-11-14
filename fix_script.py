import os
import re

file_path = r'D:\SHIKHAR_PROJECTS\2026\10 OCT\siddharth-annu-invite\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Base href and title
html = html.replace('<base href="/invites/samples/ram-mandir/">', '<base href="./">')
html = html.replace('<title>Ram Mandir | ACP Invites</title>', '<title>Siddharth & Annu | Divine Wedding Invitation</title>')

# 2. Audio path relative
html = html.replace('/invites/audio/ram-mandir-ambient.mp3', 'audio/ram-mandir-ambient.mp3')

# 3. Remove ACP branding footer
html = re.sub(r'<footer id="acp-demo-brand"[^>]*>.*?</footer>', '', html)

# 4. Remove any external tracking script that could hang the page
html = re.sub(r'<script[^>]*src="https://cp\.bestfreecdn\.com[^"]*"[^>]*>.*?</script>', '', html)

# 5. Direct text replacements throughout the file
replacements = [
    ('Sahil', 'Siddharth'),
    ('Shruti', 'Annu'),
    ('sahil', 'siddharth'),
    ('shruti', 'annu'),
    ('Akash', 'Siddharth'),
    ('Drashti', 'Annu'),
    ('akash', 'siddharth'),
    ('drashti', 'annu'),
    ('#SahilWedsShruti', '#SiddharthWedsAnnu'),
    ('#abkan', '#SiddharthWedsAnnu'),
    ('29 AUGUST 2026', '12 DECEMBER 2026'),
    ('29th Aug 2026', '12th Dec 2026'),
    ('Friday, 29th Aug', 'Saturday, 12th Dec'),
    ('Shri. Rajmani Pathak &amp; Smt. Ambika Pathak', 'Smt. Mamta &amp; Shri Shashikant Shrivastava'),
    ('Shri. Rajmani Pathak & Smt. Ambika Pathak', 'Smt. Mamta & Shri Shashikant Shrivastava'),
]
for old, new in replacements:
    html = html.replace(old, new)

# 6. Replace Gallery photos with client photos
unsplash_list = [
    'https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=400&amp;h=400&amp;fit=crop',
    'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=400&amp;h=400&amp;fit=crop',
    'https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=400&amp;h=400&amp;fit=crop',
    'https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=400&amp;h=400&amp;fit=crop',
    'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=400&amp;h=400&amp;fit=crop'
]
new_imgs = [
    'assets/couple_photo.jpg',
    'assets/card_siddharth_annu.jpg',
    'assets/card_ganesh.jpg',
    'assets/card_as_monogram.jpg',
    'assets/card_date_12dec.jpg'
]
for old, new in zip(unsplash_list, new_imgs):
    html = html.replace(old, new)

# 7. Clean, non-blocking client script (NO infinite loops)
clean_script = '''
<script>
  (function() {
    // 1. Safe text replacement helper (only changes if different)
    function safeReplace(node) {
      if (!node) return;
      if (node.nodeType === Node.TEXT_NODE) {
        let val = node.nodeValue;
        if (!val) return;
        let updated = val.replace(/Akash|Sahil/g, 'Siddharth')
                         .replace(/Drashti|Shruti/g, 'Annu')
                         .replace(/akash|sahil/g, 'siddharth')
                         .replace(/drashti|shruti/g, 'annu')
                         .replace(/#abkan|#SahilWedsShruti/g, '#SiddharthWedsAnnu')
                         .replace(/29th Aug 2026|29 AUGUST 2026/g, '12th Dec 2026')
                         .replace(/Friday, 29th Aug/g, 'Saturday, 12th Dec')
                         .replace(/Shri\\.\\s*Rajmani Pathak\\s*&amp;\\s*Smt\\.\\s*Ambika Pathak/gi, 'Smt. Mamta &amp; Shri Shashikant Shrivastava')
                         .replace(/Shri\\.\\s*Rajmani Pathak\\s*&\\s*Smt\\.\\s*Ambika Pathak/gi, 'Smt. Mamta & Shri Shashikant Shrivastava');
        if (updated !== val) {
          node.nodeValue = updated;
        }
      } else {
        for (let i = 0; i < node.childNodes.length; i++) {
          safeReplace(node.childNodes[i]);
        }
      }
    }

    // 2. Timeline Ceremonies
    const ceremonies = {
      '1': { title: 'Mehndi Ceremony', date: '10th Dec 2026', day: 'Thursday', time: '4:00 PM Onwards' },
      '2': { title: 'Haldi Ceremony', date: '11th Dec 2026', day: 'Friday', time: '10:00 AM Onwards' },
      '3': { title: 'Sangeet Night', date: '11th Dec 2026', day: 'Friday', time: '7:00 PM Onwards' },
      '4': { title: 'Shubh Vivah (Phera)', date: '12th Dec 2026', day: 'Saturday', time: '11:00 AM Onwards' },
      '5': { title: 'Grand Reception', date: '12th Dec 2026', day: 'Saturday', time: '7:00 PM Onwards' }
    };

    function updateTimelineCards() {
      for (const [key, info] of Object.entries(ceremonies)) {
        const cards = document.querySelectorAll('[data-framer-name="' + key + '"]');
        cards.forEach(card => {
          const ps = card.querySelectorAll('p.framer-text');
          ps.forEach(p => {
            const txt = p.innerText.trim();
            if (txt === 'Shaadi' && p.innerText !== info.title) {
              p.innerText = info.title;
            } else if (txt.includes('Aug') && p.innerText !== info.date) {
              p.innerText = info.date;
            } else if (txt === 'Friday' && p.innerText !== info.day) {
              p.innerText = info.day;
            } else if (txt.includes('Pm Onwards') && p.innerText !== info.time) {
              p.innerText = info.time;
            }
          });
        });
      }
    }

    // 3. Live Countdown (runs once per second only)
    const targetTime = new Date('2026-12-12T19:00:00+05:30').getTime();
    function tickCountdown() {
      const now = new Date().getTime();
      let diff = Math.max(0, targetTime - now);
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      diff %= (1000 * 60 * 60 * 24);
      const hours = Math.floor(diff / (1000 * 60 * 60));
      diff %= (1000 * 60 * 60);
      const minutes = Math.floor(diff / (1000 * 60));
      diff %= (1000 * 60);
      const seconds = Math.floor(diff / 1000);

      const dStr = String(days).padStart(2, '0');
      const hStr = String(hours).padStart(2, '0');
      const mStr = String(minutes).padStart(2, '0');
      const sStr = String(seconds).padStart(2, '0');

      const cd = document.querySelector('[data-framer-name="Countdown Timer"]');
      if (cd) {
        const spans = cd.querySelectorAll('span');
        const digits = (dStr + hStr + mStr + sStr).split('');
        if (spans.length >= 8) {
          for (let i = 0; i < 8; i++) {
            if (spans[i].innerText !== digits[i]) {
              spans[i].innerText = digits[i];
            }
          }
        }
      }
    }

    let isUpdating = false;
    function applyAll() {
      if (isUpdating) return;
      isUpdating = true;
      try {
        safeReplace(document.body);
        updateTimelineCards();
      } finally {
        isUpdating = false;
      }
    }

    document.addEventListener('DOMContentLoaded', () => {
      applyAll();
      tickCountdown();
      setInterval(tickCountdown, 1000);
      setInterval(applyAll, 1000);
    });
  })();
</script>
'''

# Replace the previous client script block
html = re.sub(r'<script>\s*\(function\(\)\s*\{\s*// 1\. Text Replacements[\s\S]*?<\/script>', lambda m: clean_script, html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with clean non-blocking code!')
