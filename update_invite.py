import os
import re

file_path = r'D:\SHIKHAR_PROJECTS\2026\10 OCT\siddharth-annu-invite\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Base href & title
html = html.replace('<base href="/invites/samples/ram-mandir/">', '<base href="./">')
html = html.replace('<title>Ram Mandir | ACP Invites</title>', '<title>Siddharth & Annu | Divine Wedding Invitation</title>')

# 2. Audio path
html = html.replace('/invites/audio/ram-mandir-ambient.mp3', 'audio/ram-mandir-ambient.mp3')

# 3. Remove ACP branding
html = html.replace('<footer id="acp-demo-brand">A.C.P · Contact: 82360 16009</footer>', '')

# 4. Gate screen
html = html.replace('Sahil<span>&amp;</span>Shruti', 'Siddharth<span>&amp;</span>Annu')
html = html.replace('29 AUGUST 2026', '12 DECEMBER 2026')

# 5. Hashtag
html = html.replace('#SahilWedsShruti', '#SiddharthWedsAnnu')
html = html.replace('#abkan', '#SiddharthWedsAnnu')

# 6. Replace Unsplash gallery photos with real couple & card assets
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

# 7. Comprehensive client script for name replacement, timeline customization and live countdown
client_script = '''
<script>
  (function() {
    // 1. Text Replacements
    function replaceNamesInNode(node) {
      if (!node) return;
      if (node.nodeType === Node.TEXT_NODE) {
        let text = node.nodeValue;
        if (text) {
          let updated = text.replace(/Akash|Sahil/g, 'Siddharth')
                            .replace(/Drashti|Shruti/g, 'Annu')
                            .replace(/akash|sahil/g, 'siddharth')
                            .replace(/drashti|shruti/g, 'annu')
                            .replace(/#abkan|#SahilWedsShruti/g, '#SiddharthWedsAnnu')
                            .replace(/29th Aug 2026|29 AUGUST 2026/g, '12th Dec 2026')
                            .replace(/Friday, 29th Aug/g, 'Saturday, 12th Dec')
                            .replace(/Shri\\.\\s*Rajmani Pathak\\s*&amp;\\s*Smt\\.\\s*Ambika Pathak/gi, 'Smt. Mamta &amp; Shri Shashikant Shrivastava')
                            .replace(/Shri\\.\\s*Rajmani Pathak\\s*&\\s*Smt\\.\\s*Ambika Pathak/gi, 'Smt. Mamta & Shri Shashikant Shrivastava');
          if (updated !== text) {
            node.nodeValue = updated;
          }
        }
      } else {
        for (let child of node.childNodes) {
          replaceNamesInNode(child);
        }
      }
    }

    // 2. Timeline Ceremonies Configuration
    const ceremonies = {
      '1': { title: 'Mehndi Ceremony', date: '10th Dec 2026', day: 'Thursday', time: '4:00 PM Onwards' },
      '2': { title: 'Haldi Ceremony', date: '11th Dec 2026', day: 'Friday', time: '10:00 AM Onwards' },
      '3': { title: 'Sangeet Night', date: '11th Dec 2026', day: 'Friday', time: '7:00 PM Onwards' },
      '4': { title: 'Shubh Vivah (Phera)', date: '12th Dec 2026', day: 'Saturday', time: '11:00 AM Onwards' },
      '5': { title: 'Grand Reception', date: '12th Dec 2026', day: 'Saturday', time: '7:00 PM Onwards' }
    };

    function updateTimelineCards() {
      for (const [key, info] of Object.entries(ceremonies)) {
        const cards = document.querySelectorAll(`[data-framer-name="${key}"]`);
        cards.forEach(card => {
          const ps = card.querySelectorAll('p.framer-text');
          ps.forEach(p => {
            const txt = p.innerText.trim();
            if (txt === 'Shaadi' || txt.includes('Ceremony') || txt.includes('Night') || txt.includes('Vivah') || txt.includes('Reception')) {
              p.innerText = info.title;
            } else if (txt.includes('Aug') || txt.includes('Dec')) {
              p.innerText = info.date;
            } else if (txt === 'Friday' || txt === 'Saturday' || txt === 'Thursday') {
              p.innerText = info.day;
            } else if (txt.includes('Pm Onwards') || txt.includes('AM Onwards') || txt.includes('PM Onwards')) {
              p.innerText = info.time;
            }
          });
        });
      }
    }

    // 3. Live Countdown to 12 December 2026, 7:00 PM
    const targetTime = new Date('2026-12-12T19:00:00+05:30').getTime();
    function updateCountdown() {
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

      const cdContainer = document.querySelector('[data-framer-name="Countdown Timer"]');
      if (cdContainer) {
        const digitSpans = cdContainer.querySelectorAll('span');
        const digits = (dStr + hStr + mStr + sStr).split('');
        if (digitSpans.length >= 8) {
          for (let i = 0; i < 8; i++) {
            digitSpans[i].innerText = digits[i];
          }
        }
      }
    }

    function scanAndApply() {
      replaceNamesInNode(document.body);
      updateTimelineCards();
      updateCountdown();
    }

    document.addEventListener('DOMContentLoaded', scanAndApply);
    window.addEventListener('load', scanAndApply);
    setInterval(scanAndApply, 250);

    const observer = new MutationObserver(scanAndApply);
    observer.observe(document.documentElement, { childList: true, subtree: true, characterData: true });
  })();
</script>
'''

pattern = r'<script>\s*\(function\(\)\s*\{\s*function replaceNamesInNode[\s\S]*?<\/script>'
html = re.sub(pattern, lambda m: client_script, html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Client script and timeline updated successfully!')
