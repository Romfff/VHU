/**
 * Đại học Văn Hiến (VHU) Admissions Portal Application
 * Interactivity: 44 Majors Directory, GPA & Tuition Calculator, Registration Modal
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Navigation & Scroll Header
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // 2. Mobile Drawer Navigation
  const burger = document.querySelector('.burger');
  const drawer = document.querySelector('.drawer');
  if (burger && drawer) {
    burger.addEventListener('click', () => {
      const isOpen = drawer.classList.toggle('is-open');
      burger.classList.toggle('is-active', isOpen);
      burger.setAttribute('aria-expanded', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    drawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.remove('is-open');
        burger.classList.remove('is-active');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // 3. Faculty Spotlight Interactive Rows
  const spotlightData = {
    'ai-tech': {
      badge: 'Công Nghệ Tiên Phong 2026',
      title: 'Khoa Công Nghệ Thông Tin & AI',
      desc: 'Chương trình đào tạo đón đầu làn sóng cách mạng công nghiệp 4.0 với phòng thực hành AI & Cloud Computing hiện đại, hợp tác trực tiếp cùng Microsoft, Google Cloud và AWS.',
      features: [
        'Lab Trí tuệ Nhân tạo thế hệ mới với hạ tầng GPU chuyên sâu',
        'Thực tập trực tiếp tại các công ty công nghệ thuộc HungHau Holdings',
        'Cam kết 100% sinh viên có việc làm mức lương khởi điểm từ 12-25 triệu/tháng'
      ],
      majors: 'Trí tuệ nhân tạo (AI), Kỹ thuật phần mềm, An ninh mạng, KH máy tính',
      img: 'assets/images/i4.aa7da4922ed28ffbd26c.webp'
    },
    'business': {
      badge: 'Đào Tạo Doanh Nhân Thực Chiến',
      title: 'Khoa Kinh Tế & Quản Trị Kinh Doanh',
      desc: 'Mô hình giảng dạy kết nối doanh nghiệp từ năm 2. Sinh viên được trải nghiệm điều hành doanh nghiệp thực tế, giao dịch chứng khoán mô phỏng và quản trị chuỗi cung ứng quốc tế.',
      features: [
        'Mạng lưới 500+ doanh nghiệp đối tác tuyển dụng thường niên',
        'Thực tập hưởng lương ngay từ học kỳ thứ 4',
        'Học kỳ doanh nghiệp và đào tạo kỹ năng lãnh đạo thực tế'
      ],
      majors: 'Logistics, Marketing số, Quản trị kinh doanh, Tài chính - Ngân hàng, TMĐT',
      img: 'assets/images/i2.89ee825551a01d8e5ce6.webp'
    },
    'tourism': {
      badge: 'Chuẩn Nghề Quốc Tế 5 Sao',
      title: 'Khoa Du Lịch & Khách Sạn',
      desc: 'Hệ thống phòng thực hành mô phỏng khách sạn 5 sao ngay trong khuôn viên trường. Chương trình thực tập và cơ hội việc làm quốc tế tại Nhật Bản, Singapore, Dubai.',
      features: [
        'Phòng buồng phòng, Barista, Lễ tân chuẩn quốc tế',
        'Tour trải nghiệm thực tế xuyên Việt từ năm thứ nhất',
        'Chứng chỉ nghiệp vụ được các chuỗi khách sạn quốc tế công nhận'
      ],
      majors: 'Quản trị khách sạn, Lữ hành du lịch, Quản trị nhà hàng & dịch vụ ăn uống',
      img: 'assets/images/i8.411a68782c270ab991ca.webp'
    },
    'languages': {
      badge: 'Công Dân Toàn Cầu',
      title: 'Khoa Ngôn Ngữ & Văn Hóa Quốc Tế',
      desc: 'Đào tạo ngôn ngữ kết hợp kỹ năng thương mại và giao lưu văn hóa chuyên sâu. Sinh viên tốt nghiệp đạt chuẩn ngoại ngữ C1/IELTS 6.5+, HSK 5, JLPT N2, TOPIK 4.',
      features: [
        '100% giảng viên bản xứ tham gia giảng dạy kỹ năng nghe nói',
        'Học bổng trao đổi học tập tại Nhật Bản, Hàn Quốc, Pháp',
        'Làm việc ngay tại các tập đoàn FDI đa quốc gia tại Việt Nam'
      ],
      majors: 'Ngôn ngữ Anh, Ngôn ngữ Trung Quốc, Ngôn ngữ Nhật, Ngôn ngữ Hàn Quốc, Ngôn ngữ Pháp',
      img: 'assets/images/i5.9bcb64c7cdb16a84e174.webp'
    },
    'arts': {
      badge: 'Sáng Tạo Nghệ Thuật & Truyền Thông',
      title: 'Khoa Nghệ Thuật & Truyền Thông Đa Phương Tiện',
      desc: 'Nhà hát Beethoven sang trọng, studio phim trường chuyên nghiệp, phòng thu âm và dàn nhạc cụ hiện đại bậc nhất TP.HCM với sự đồng hành của các nghệ sĩ, đạo diễn đầu ngành.',
      features: [
        'Hội trường Beethoven sức chứa lớn, âm thanh vòm chuẩn rạp hát',
        'Studio quay dựng, phòng biên tập video và đồ họa kỹ xảo VFX',
        'Cơ hội biểu diễn nghệ thuật và sản xuất tác phẩm chuyên nghiệp'
      ],
      majors: 'Thanh nhạc, Piano, Đạo diễn điện ảnh, Truyền thông đa phương tiện, Thiết kế đồ họa',
      img: 'assets/images/i40.8835ce749c623e075559.webp'
    }
  };

  const glowRows = document.querySelectorAll('.glow__row');
  const glowShowcase = document.getElementById('glowShowcase');

  function updateSpotlight(key) {
    const data = spotlightData[key];
    if (!data || !glowShowcase) return;

    glowShowcase.innerHTML = `
      <div class="glow__showcase-card">
        <span class="glow__badge">${data.badge}</span>
        <h3 class="glow__card-title">${data.title}</h3>
        <p class="glow__card-desc">${data.desc}</p>
        <ul class="glow__card-features">
          ${data.features.map(f => `<li>${f}</li>`).join('')}
        </ul>
        <div style="border-top: 1px solid var(--rule-on-brand); padding-top: 18px; margin-top: 18px;">
          <p style="font-size: 12px; font-weight: 600; text-transform: uppercase; color: var(--on-brand-dim); margin-bottom: 6px;">Các ngành trọng điểm:</p>
          <p style="font-size: 14px; color: var(--accent-bright); font-weight: 500;">${data.majors}</p>
        </div>
        <div style="margin-top: 24px;">
          <a href="#catalogue" class="btn btn--outlineBrand" style="padding: 10px 20px; font-size: 12px;">Xem danh sách ngành →</a>
        </div>
      </div>
    `;
  }

  glowRows.forEach(row => {
    row.addEventListener('click', () => {
      glowRows.forEach(r => r.classList.remove('is-active'));
      row.classList.add('is-active');
      const key = row.getAttribute('data-faculty');
      updateSpotlight(key);
    });
  });

  // 4. Render 44 Majors Directory with Live Search & Tabs
  const majorsGrid = document.getElementById('majorsGrid');
  const searchInput = document.getElementById('majorSearchInput');
  const tabButtons = document.querySelectorAll('.tab-btn');
  const majorCountDisplay = document.getElementById('majorCountDisplay');

  let currentCategory = 'all';
  let searchQuery = '';

  function formatCurrency(num) {
    return new Intl.NumberFormat('vi-VN').format(num) + ' đ';
  }

  function renderMajors() {
    if (!majorsGrid) return;

    let filtered = VHU_MAJORS;

    if (currentCategory !== 'all') {
      filtered = filtered.filter(m => m.category === currentCategory);
    }

    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase().trim();
      filtered = filtered.filter(m => 
        m.name.toLowerCase().includes(q) || 
        m.code.toLowerCase().includes(q) ||
        m.categoryName.toLowerCase().includes(q)
      );
    }

    if (majorCountDisplay) {
      majorCountDisplay.textContent = `Hiển thị ${filtered.length} / ${VHU_MAJORS.length} ngành`;
    }

    if (filtered.length === 0) {
      majorsGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; background: #fff; border-radius: 10px; border: 1px dashed var(--rule-strong);">
          <p style="font-family: var(--font-serif); font-size: 24px; color: var(--ink); margin-bottom: 8px;">Không tìm thấy ngành đào tạo phù hợp</p>
          <p style="font-size: 14px; color: var(--ink-3);">Quý phụ huynh và học sinh vui lòng thử tìm kiếm với từ khóa khác hoặc gọi Hotline 1800 1568 để được hỗ trợ.</p>
        </div>
      `;
      return;
    }

    majorsGrid.innerHTML = filtered.map(m => `
      <div class="major-card">
        <div class="major-card__top">
          <div class="major-card__meta">
            <span class="major-card__code">Mã ngành: ${m.code}</span>
            <span class="major-card__group">${m.group}</span>
          </div>
          <h3 class="major-card__title">${m.name}</h3>
          <p class="major-card__desc">${m.highlights || m.description}</p>
        </div>

        <div>
          <div class="major-card__pricing">
            <div class="pricing-row pricing-row--original">
              <span>Học phí gốc HK1:</span>
              <span>${formatCurrency(m.fee)}</span>
            </div>
            <div class="pricing-row" style="margin-top: 6px; align-items: baseline;">
              <span style="font-size: 13px; font-weight: 600; color: #334155; white-space: nowrap;">Học phí HK1 (-50%):</span>
              <span class="pricing-discount-val">${formatCurrency(m.feeDiscount)}</span>
            </div>
          </div>

          <div class="major-card__footer">
            <span class="major-card__credits">
              ${m.credits} tín chỉ (4 năm)
            </span>
            <button class="major-card__action" onclick="openMajorModal(${m.id})">
              Xem chi tiết <span style="font-size: 14px;">→</span>
            </button>
          </div>
        </div>
      </div>
    `).join('');
  }

  // Bind tab click events
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tabButtons.forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');
      currentCategory = btn.getAttribute('data-cat');
      renderMajors();
    });
  });

  // Bind search input events
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderMajors();
    });
  }

  // Populate major select dropdowns
  const calcMajorSelect = document.getElementById('calcMajor');
  const formMajorSelect = document.getElementById('formMajor');

  if (calcMajorSelect) {
    VHU_MAJORS.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.id;
      opt.textContent = `${m.name} (Mã: ${m.code})`;
      calcMajorSelect.appendChild(opt);
    });
  }

  if (formMajorSelect) {
    VHU_MAJORS.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.name;
      opt.textContent = `${m.name} (${m.code})`;
      formMajorSelect.appendChild(opt);
    });
  }

  // 5. Interactive Admission Calculator Logic
  const calcScore1 = document.getElementById('score1');
  const calcScore2 = document.getElementById('score2');
  const calcScore3 = document.getElementById('score3');
  const calcMethod = document.getElementById('calcMethod');
  const resultScoreVal = document.getElementById('resultScoreVal');
  const resultStatus = document.getElementById('resultStatus');
  const resultMajorName = document.getElementById('resultMajorName');
  const resultRawFee = document.getElementById('resultRawFee');
  const resultDiscountFee = document.getElementById('resultDiscountFee');

  function calculateScore() {
    const s1 = parseFloat(calcScore1.value) || 0;
    const s2 = parseFloat(calcScore2.value) || 0;
    const s3 = parseFloat(calcScore3.value) || 0;
    const total = (s1 + s2 + s3);

    const selectedMajorId = parseInt(calcMajorSelect.value);
    const major = VHU_MAJORS.find(m => m.id === selectedMajorId) || VHU_MAJORS[0];

    if (resultScoreVal) {
      resultScoreVal.innerHTML = `${total.toFixed(2)} <span>/ 30</span>`;
    }

    if (resultMajorName) {
      resultMajorName.textContent = major.name;
    }

    if (resultRawFee) {
      resultRawFee.textContent = formatCurrency(major.fee);
    }

    if (resultDiscountFee) {
      resultDiscountFee.textContent = formatCurrency(major.feeDiscount);
    }

    if (resultStatus) {
      if (total >= 18.0) {
        resultStatus.innerHTML = `
          <span style="color: #4ade80;">●</span> Đủ điều kiện trúng tuyển sớm (Học bạ ≥ 18.0 điểm)
        `;
        resultStatus.style.color = '#4ade80';
      } else if (total > 0) {
        resultStatus.innerHTML = `
          <span style="color: #facc15;">●</span> Dự kiến cần bổ sung điểm hoặc xét các phương thức khác
        `;
        resultStatus.style.color = '#facc15';
      } else {
        resultStatus.innerHTML = `
          <span style="color: var(--on-brand-dim);">●</span> Nhập điểm để kiểm tra điều kiện xét tuyển
        `;
        resultStatus.style.color = 'var(--on-brand-dim)';
      }
    }
  }

  [calcScore1, calcScore2, calcScore3, calcMajorSelect, calcMethod].forEach(el => {
    if (el) el.addEventListener('input', calculateScore);
  });

  // Initial calculation and render
  calculateScore();
  renderMajors();

  // 6. Major Detail Modal Logic
  const majorModal = document.getElementById('majorModal');
  const modalMajorTitle = document.getElementById('modalMajorTitle');
  const modalMajorContent = document.getElementById('modalMajorContent');

  window.openMajorModal = function(id) {
    const major = VHU_MAJORS.find(m => m.id === id);
    if (!major || !majorModal) return;

    modalMajorTitle.textContent = `${major.name} - Mã ngành: ${major.code}`;
    modalMajorContent.innerHTML = `
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div style="background: var(--paper-2); padding: 18px 22px; border-radius: 8px; border-left: 4px solid var(--vhu-blue);">
          <p style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: var(--ink-3); margin-bottom: 4px;">Khoa & Nhóm ngành</p>
          <p style="font-size: 16px; font-weight: 700; color: var(--ink);">${major.categoryName} (${major.group})</p>
        </div>

        <div>
          <h4 style="font-family: var(--font-serif); font-size: 19px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">Tổ hợp môn xét tuyển 2026:</h4>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 6px;">
            ${major.combinations.map(c => `
              <li style="font-size: 14.5px; color: var(--ink-2); display: flex; align-items: center; gap: 8px;">
                <span style="color: var(--vhu-blue); font-weight: bold;">▪</span> ${c}
              </li>
            `).join('')}
          </ul>
        </div>

        <div>
          <h4 style="font-family: var(--font-serif); font-size: 19px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">Điểm nổi bật chương trình:</h4>
          <p style="font-size: 14.5px; color: var(--ink-2); line-height: 1.65;">${major.highlights}</p>
        </div>

        <div>
          <h4 style="font-family: var(--font-serif); font-size: 19px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">Cơ hội nghề nghiệp sau tốt nghiệp:</h4>
          <p style="font-size: 14.5px; color: var(--ink-2); line-height: 1.65;">${major.careers}</p>
        </div>

        <div style="border-top: 1px solid var(--rule); padding-top: 18px; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div>
            <p style="font-size: 12px; font-weight: 600; color: var(--ink-3); text-transform: uppercase;">Số tín chỉ tích lũy</p>
            <p style="font-family: var(--font-sans); font-size: 24px; color: var(--ink); font-weight: 800;">${major.credits} tín chỉ</p>
          </div>
          <div>
            <p style="font-size: 12px; font-weight: 600; color: var(--ink-3); text-transform: uppercase;">Học phí HK1 sau hỗ trợ 50%</p>
            <p style="font-family: var(--font-sans); font-size: 24px; color: var(--vhu-blue); font-weight: 800;">${formatCurrency(major.feeDiscount)}</p>
          </div>
        </div>

        <div style="margin-top: 10px; display: flex; gap: 12px; justify-content: flex-end;">
          <button class="btn btn--outlineDark" onclick="closeModal('majorModal')">Đóng</button>
          <a href="#dangky" class="btn btn--solid" onclick="selectMajorForRegistration('${major.name}')">Đăng ký ngành này →</a>
        </div>
      </div>
    `;
    majorModal.classList.add('is-active');
  };

  window.selectMajorForRegistration = function(majorName) {
    closeModal('majorModal');
    if (formMajorSelect) {
      formMajorSelect.value = majorName;
    }
  };

  window.closeModal = function(id) {
    const m = document.getElementById(id);
    if (m) m.classList.remove('is-active');
  };

  // Close modals on ESC or clicking outside
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('is-active'));
    }
  });

  document.querySelectorAll('.modal-overlay').forEach(m => {
    m.addEventListener('click', (e) => {
      if (e.target === m) {
        m.classList.remove('is-active');
      }
    });
  });

  // 7. Admission Registration Form Submission Simulation
  const regForm = document.getElementById('admissionsForm');
  const successModal = document.getElementById('successModal');
  const regRefNumber = document.getElementById('regRefNumber');
  const regCandidateName = document.getElementById('regCandidateName');
  const regCandidateMajor = document.getElementById('regCandidateMajor');

  if (regForm) {
    regForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const fullName = document.getElementById('formFullName').value.trim();
      const phone = document.getElementById('formPhone').value.trim();
      const major = document.getElementById('formMajor').value;

      if (!fullName || !phone) {
        alert('Vui lòng nhập đầy đủ Họ và tên và Số điện thoại liên hệ.');
        return;
      }

      // Generate simulated reference registration code
      const refCode = 'VHU-2026-' + Math.floor(100000 + Math.random() * 900000);

      if (regRefNumber) regRefNumber.textContent = refCode;
      if (regCandidateName) regCandidateName.textContent = fullName;
      if (regCandidateMajor) regCandidateMajor.textContent = major;

      if (successModal) {
        successModal.classList.add('is-active');
      }

      regForm.reset();
    });
  }

  // Pre-fill calculator values button
  const prefillCalcBtn = document.getElementById('prefillCalcBtn');
  if (prefillCalcBtn) {
    prefillCalcBtn.addEventListener('click', () => {
      calcScore1.value = 8.5;
      calcScore2.value = 7.5;
      calcScore3.value = 8.0;
      calculateScore();
    });
  }
});
