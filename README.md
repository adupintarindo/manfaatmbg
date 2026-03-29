# Manfaat MBG - Indonesia's Free Nutritious Meals Program Dashboard

A comprehensive, interactive data visualization dashboard for Indonesia's MBG (Makan Bergizi Gratis / Free Nutritious Meals) program. This single-file HTML application provides national and provincial-level insights into nutrition program delivery across all 38 Indonesian provinces.

## Features

### 1. **Interactive Indonesia SVG Map**
- Clickable provinces with color-coded intensity visualization
- SPPG (School Feeding Program Kitchen) counts determine color depth
- Hover tooltips showing province statistics
- Click to open detailed province-specific sidebar
- Responsive layout suitable for all screen sizes

### 2. **National Summary Dashboard**
- Total SPPG: 25,495 kitchens nationwide
- Total Beneficiaries: ~2.3M people
- Total Fund Distributed: ~Rp 15.9T
- Total Provinces: 38
- Total Districts/Cities (Kabupaten/Kota): 498
- Days Running since program start

### 3. **Beneficiary Breakdown**
- Large visual display of total beneficiaries
- Three-category breakdown:
  - **Siswa/i Sekolah (School Students)**: 1.76M
  - **Ibu Hamil & Menyusui (Pregnant & Nursing Mothers)**: 334K
  - **Balita 0-59 Bulan (Toddlers)**: 286K
- Interactive donut chart in province sidebar

### 4. **Province Sidebar Details**
Clicking any province reveals comprehensive data:
- SPPG and beneficiary counts
- Daily and total fund allocation
- Worker statistics (kitchen, local, suppliers, drivers)
- School count
- Beneficiary breakdown with visualization
- Monthly financial flow (commodity, worker, transport costs)
- Monthly commodity requirements (carbs, side dishes, fruits, vegetables, spices)
- Detailed list of all districts/cities in province with SPPG counts

### 5. **Search & Navigation**
- Dropdown province selector for quick navigation
- Scrolls to map and opens sidebar for selected province
- Language toggle (Indonesian/English)

### 6. **Data Visualization**
- Three interactive Chart.js charts:
  1. **Beneficiary Distribution (Donut)** - Visual breakdown by category
  2. **Monthly Fund Flow (Horizontal Bar)** - Commodity, worker, and transport costs
  3. **Monthly Commodity Needs (Bar)** - Tons required by commodity type

### 7. **Swiss/International Design Aesthetic**
- Clean, grid-driven layout
- Information-dense but uncluttered
- Professional institutional appearance
- Fonts: Satoshi (headings), Plus Jakarta Sans (body) - via Google Fonts
- Color Palette:
  - Primary: Deep teal (#0D6E6E)
  - Accents: Coral, Green, Blue, Pink, Orange for data categories
  - Clean whites and subtle grays

### 8. **Responsive Design**
- Mobile-first approach
- Adapts from 480px smartphones to 1600px+ wide screens
- Touch-friendly sidebar on mobile
- Optimized tooltip positioning

### 9. **Multilingual Support**
- Indonesian (Bahasa Indonesia) - Default
- English
- Toggle button in header
- All UI text translatable

## Technical Specifications

### Technology Stack
- **HTML5** with semantic structure
- **CSS3** with CSS Variables for theming
- **Vanilla JavaScript** (no frameworks required)
- **Chart.js** for data visualization (CDN)
- **Google Fonts** for typography (CDN)

### File Size
- Complete HTML: ~292 KB (includes all data)
- No build step required
- No external dependencies beyond CDN resources

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment

### Local Development
```bash
npm install
npm run dev
# Serves on http://localhost:3000
```

### Vercel Deployment
```bash
vercel deploy
```

The `vercel.json` configuration:
- Routes all requests to `index.html`
- Regions: Singapore, Sydney (optimized for Southeast Asia)
- Static site deployment - zero server-side processing

### Direct Deployment
Simply serve `index.html` from any static web server:
- Apache
- Nginx
- AWS S3 + CloudFront
- GitHub Pages
- Netlify
- Any CDN

## Data Structure

The JSON data is embedded inline in the HTML. Structure:

```json
{
  "national": {
    "sppg": 25495,
    "beneficiaries": 2385191,
    "students": 1765041,
    "mothers": 333927,
    "toddlers": 286223,
    "kitchenWorkers": 27454,
    "localWorkers": 32927,
    "suppliers": 8683,
    "drivers": 8334,
    "nutritionists": 947,
    "schools": 21356,
    "monthlyTons": 22512.1,
    "carbs": 4206.7,
    "sidedish": 1708.2,
    "fruits": 11294.3,
    "vegetables": 2600.5,
    "spices": 2702.5,
    "monthlyCommodityCost": 956062000,
    "monthlyWorkerCost": 91782000,
    "monthlyTransportCost": 23965000,
    "monthlyTotalCost": 1071809000,
    "dailyFund": 35693000,
    "totalFund": 15954771000,
    "provinces": 38,
    "kabupatenCount": 498
  },
  "provinces": {
    "PROVINCE_NAME": {
      "...all fields as above...": 0,
      "kabupaten": {
        "DISTRICT_NAME": { "...data..." }
      }
    }
  },
  "meta": {
    "totalSPPG": 25495,
    "totalProvinces": 38,
    "dataDate": "28 Maret 2026",
    "programStart": "6 Januari 2025",
    "daysRunning": 447
  }
}
```

## Key Metrics (National Level)

- **Total SPPG (School Feeding Kitchens)**: 25,495
- **Total Beneficiaries**: 2,385,191
- **Students**: 1,765,041 (74%)
- **Pregnant & Nursing Mothers**: 333,927 (14%)
- **Toddlers (0-59 months)**: 286,223 (12%)
- **Kitchen Workers**: 27,454
- **Local Workers**: 32,927
- **Suppliers**: 8,683
- **Drivers**: 8,334
- **Schools Covered**: 21,356
- **Monthly Commodity Requirement**: 22,512 tons
- **Total Fund Distributed**: Rp 15.9 Trillion
- **Days Operating**: 447 (as of March 28, 2026)

## Customization

### Updating Data
Replace the embedded JSON in the `<script>` section with new data from `mbg_stats.json`.

### Changing Colors
Edit CSS variables in `:root`:
```css
--primary: #0D6E6E;
--accent-coral: #FF6B6B;
--accent-blue: #3B82F6;
```

### Adding Languages
Add translation objects to the `translations` object in the JavaScript section.

### Modifying Chart Styling
Chart.js options are configurable in:
- `drawBeneficiaryChart()`
- `drawMonthlyFlowChart()`
- `drawCommodityChart()`

## Performance Notes

- **Initial Load**: ~2-3s on 3G, <1s on broadband
- **Map Rendering**: 38 province regions, optimized with CSS
- **Charts**: Lazy-loaded on sidebar open
- **Memory**: ~10-15 MB total (including data)
- **Mobile Optimization**: Sidebar slides from right, overlay prevents body scroll

## Accessibility Features

- Semantic HTML structure
- ARIA labels on form controls
- Color contrast ratio 7:1+ (WCAG AAA)
- Keyboard navigation support
- Focus visible indicators

## Future Enhancements

- Time-series data visualization
- Province comparison tools
- Export to PDF/Excel
- Real-time data integration
- Advanced filtering & search
- Regional grouping (Sumatra, Java, etc.)
- Infrastructure overlay (map of kitchens)

## Support & Maintenance

For updates to national or provincial data:
1. Update `mbg_stats.json`
2. Regenerate HTML with embedded data
3. Deploy to hosting

For feature requests or bug reports, document in issue tracker.

---

**Program**: Makan Bergizi Gratis (MBG) / Free Nutritious Meals
**Data Date**: March 28, 2026
**Program Start**: January 6, 2025
**Total Coverage**: 38 Provinces, 498 Districts/Cities
