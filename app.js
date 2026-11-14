/* ==========================================================================
   RAM MANDIR DIVINE WEDDING INTERACTIVE JAVASCRIPT
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initCountdown();
  initAudioPlayer();
  initHashtagCopy();
  initRSVPForm();
  initParticleCanvas();
  initScrollReveal();
});

/* ==========================================================================
   1. LIVE COUNTDOWN TIMER
   ========================================================================== */
function initCountdown() {
  // Target Wedding Date: August 29, 2026 18:00:00 (6 PM IST)
  const targetDate = new Date('2026-08-29T18:00:00+05:30').getTime();

  const daysEl = document.getElementById('days');
  const hoursEl = document.getElementById('hours');
  const minutesEl = document.getElementById('minutes');
  const secondsEl = document.getElementById('seconds');

  function updateTimer() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance < 0) {
      daysEl.innerText = '00';
      hoursEl.innerText = '00';
      minutesEl.innerText = '00';
      secondsEl.innerText = '00';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    daysEl.innerText = days < 10 ? '0' + days : days;
    hoursEl.innerText = hours < 10 ? '0' + hours : hours;
    minutesEl.innerText = minutes < 10 ? '0' + minutes : minutes;
    secondsEl.innerText = seconds < 10 ? '0' + seconds : seconds;
  }

  updateTimer();
  setInterval(updateTimer, 1000);
}

/* ==========================================================================
   2. ETHEREAL DEVOTIONAL SYNTHESIZER AUDIO PLAYER (Web Audio API)
   ========================================================================== */
function initAudioPlayer() {
  const audioBtn = document.getElementById('audioToggleBtn');
  const audioText = document.getElementById('audioText');

  let audioCtx = null;
  let isPlaying = false;
  let oscillators = [];
  let masterGain = null;

  function createDevotionalSound() {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    masterGain = audioCtx.createGain();
    masterGain.gain.value = 0.15; // Soft gentle ambient background volume
    masterGain.connect(audioCtx.destination);

    // Ethereal Indian Tanpura / Flute Harmonics (Sa-Pa drone frequencies: C# / G# / C#)
    const frequencies = [277.18, 415.30, 554.37, 830.61];

    frequencies.forEach((freq, index) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.type = index % 2 === 0 ? 'sine' : 'triangle';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      // Subtle vibrato/swell animation for flute harmonic effect
      const lfo = audioCtx.createOscillator();
      const lfoGain = audioCtx.createGain();
      lfo.frequency.value = 0.2 + index * 0.1; // Gentle pulsation
      lfoGain.gain.value = 3;
      lfo.connect(osc.frequency);
      lfo.start();

      gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
      osc.connect(gain);
      gain.connect(masterGain);
      osc.start();

      oscillators.push({ osc, lfo });
    });
  }

  audioBtn.addEventListener('click', () => {
    if (!audioCtx) {
      createDevotionalSound();
      isPlaying = true;
      audioBtn.classList.remove('muted');
      audioText.innerText = 'Music Playing';
      showToast('🎶 Divine Flute Ambient Music Playing');
      return;
    }

    if (isPlaying) {
      audioCtx.suspend();
      isPlaying = false;
      audioBtn.classList.add('muted');
      audioText.innerText = 'Music Muted';
      showToast('🔇 Music Muted');
    } else {
      audioCtx.resume();
      isPlaying = true;
      audioBtn.classList.remove('muted');
      audioText.innerText = 'Music Playing';
      showToast('🎶 Music Playing');
    }
  });
}

/* ==========================================================================
   3. HASHTAG COPY TO CLIPBOARD
   ========================================================================== */
function initHashtagCopy() {
  const copyBtn = document.getElementById('copyHashtagBtn');
  if (!copyBtn) return;

  copyBtn.addEventListener('click', () => {
    const hashtag = '#SahilWedsShruti';
    navigator.clipboard.writeText(hashtag).then(() => {
      showToast('✨ Hashtag #SahilWedsShruti copied to clipboard!');
    }).catch(() => {
      showToast('Hashtag: #SahilWedsShruti');
    });
  });
}

/* ==========================================================================
   4. WHATSAPP RSVP FORM GENERATOR
   ========================================================================== */
function initRSVPForm() {
  const rsvpForm = document.getElementById('rsvpForm');
  if (!rsvpForm) return;

  rsvpForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('guestName').value.trim();
    const event = document.getElementById('eventSelect').value;
    const count = document.getElementById('guestCount').value;
    const wishes = document.getElementById('wishesMsg').value.trim();

    if (!name) {
      alert('Please enter your full name');
      return;
    }

    let message = `*Divine Wedding RSVP for Sahil & Shruti*%0A%0A`;
    message += `*Guest Name:* ${encodeURIComponent(name)}%0A`;
    message += `*Attending Event:* ${encodeURIComponent(event)}%0A`;
    message += `*No. of Guests:* ${encodeURIComponent(count)}%0A`;

    if (wishes) {
      message += `*Message/Wishes:* ${encodeURIComponent(wishes)}%0A`;
    }

    message += `%0A*Looking forward to celebrating Jai Shri Ram!* 🪷✨`;

    // WhatsApp API URL (Opens chat or web whatsapp)
    const whatsappUrl = `https://api.whatsapp.com/send?text=${message}`;

    showToast('🚀 Redirecting to WhatsApp RSVP...');
    setTimeout(() => {
      window.open(whatsappUrl, '_blank');
    }, 800);
  });
}

/* ==========================================================================
   5. TOAST NOTIFICATION UTILITY
   ========================================================================== */
function showToast(msg) {
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toastMsg');
  if (!toast || !toastMsg) return;

  toastMsg.innerText = msg;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

/* ==========================================================================
   6. FALLING GOLDEN LOTUS & DIYA SPARKLE CANVAS
   ========================================================================== */
function initParticleCanvas() {
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const particleCount = 35;

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      radius: Math.random() * 3 + 1,
      color: Math.random() > 0.3 ? 'rgba(212, 175, 55, ' : 'rgba(247, 232, 212, ',
      opacity: Math.random() * 0.7 + 0.3,
      speedY: Math.random() * 0.8 + 0.2,
      speedX: Math.sin(Math.random() * Math.PI) * 0.5,
      angle: Math.random() * Math.PI * 2,
    });
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    particles.forEach((p) => {
      p.y += p.speedY;
      p.x += Math.sin(p.angle) * 0.4;
      p.angle += 0.01;

      if (p.y > height) {
        p.y = -10;
        p.x = Math.random() * width;
      }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color + p.opacity + ')';
      ctx.shadowBlur = 10;
      ctx.shadowColor = '#d4af37';
      ctx.fill();
    });

    requestAnimationFrame(animate);
  }

  animate();
}

/* ==========================================================================
   7. SCROLL REVEAL ANIMATION OBSERVER
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll(
    '.mandir-arch-card, .mandap-card-wrapper, .scalloped-badge-card, .couple-walk-card-wrapper, .ram-spire-container, .section-header, .couple-grid, .timer-box, .event-card, .info-card, .map-card-wrapper, .rsvp-card-wrapper'
  );

  revealElements.forEach((el) => {
    el.classList.add('reveal-item');
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
        }
      });
    },
    { threshold: 0.12 }
  );

  revealElements.forEach((el) => observer.observe(el));
}

