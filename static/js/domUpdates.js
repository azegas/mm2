export function updateStockData(data) {
    const stockDiv = document.getElementById('stock_data');
    if (stockDiv) {
        stockDiv.innerHTML = ''; // Clear previous content
        
        const stockCards = document.createElement('div');
        stockCards.className = 'stock-cards';
        
        Object.entries(data.stocks).forEach(([symbol, details]) => {
            const stockCard = document.createElement('div');
            stockCard.className = 'stock-card';
            stockCard.innerHTML = `
                <div class="stock-info">
                    <div class="row">
                        <span class="symbol">${symbol}</span>
                        <span class="data">
                            <span class="price-container">
                                <span class="price">$${details.price}</span>
                                <span class="change">${details.change}</span>
                                <span class="change-percent">${details.change_percent}</span>
                            </span>
                        </span>
                    </div>
                </div>
            `;
            stockCards.appendChild(stockCard);
        });
        
        stockDiv.appendChild(stockCards);

        // Add timestamp for all stock data
        const timestampElement = document.createElement('p');
        timestampElement.className = 'stock-timestamp timestamp';
        timestampElement.textContent = `Stocks updated at: ${data.timestamp}`;
        stockDiv.appendChild(timestampElement);
    }
}
export function updateSensorData(data) {
    const sensorDataDiv = document.getElementById('sensor_data');
    if (sensorDataDiv) {
        sensorDataDiv.innerHTML = ''; // Clear previous content

        sensorDataDiv.innerHTML = `
            <span class="sensor-data-value">${data.temperature} °C</span>
            <span class="sensor-data-value">${data.humidity} %</span>
        `;
    }
}
          
export function updateTextColors(data) {
    document.querySelectorAll('.change, .change-percent').forEach(element => {
        const text = element.textContent.trim();
        if (text.includes('-')) {
            element.classList.add("red-text");
        } else if (text.includes('+')) {
            element.classList.add("green-text");
        }
    });
}

export function updateCvbankasData(data) {
    const jobsContainer = document.getElementById('cvbankas_jobs');
    jobsContainer.innerHTML = ''; // Clear previous content
    
    const jobCards = document.createElement('div');
    jobCards.className = 'job-cards';
    
    data.jobs.forEach(job => {
        const card = document.createElement('div');
        card.className = 'job-card';
        card.innerHTML = `
            <div class="job-info">
                <div class="row">
                    <span class="job-title">${job.title}</span>
                    <span class="data">
                        <span class="job-company">${job.company}</span>
                        <span class="job-salary">${job.salary}</span>
                    </span>
                </div>
            </div>
        `;
        jobCards.appendChild(card);
    });
    
    jobsContainer.appendChild(jobCards);

    // Add timestamp at the bottom of all jobs
    const timestampElement = document.createElement('p');
    timestampElement.className = 'timestamp';
    timestampElement.textContent = `Jobs updated at: ${data.fetch_date}`;
    jobsContainer.appendChild(timestampElement);
}

export function updateSystemInfo(data) {
    const systemInfoDiv = document.getElementById('system_info');
    if (systemInfoDiv) {
        systemInfoDiv.innerHTML = ''; // Clear previous content
        systemInfoDiv.innerHTML = `<span>CPU: ${data.cpu_usage}% | RAM: ${data.memory_usage}% | Temp: ${data.temperature} °C | Uptime: ${data.uptime} | <span class="timestamp">Updated: ${data.timestamp}</span></span>`;
    }
}


export function updateCurrentTime() {
    const currentTimeElement = document.getElementById('current-time');
    if (currentTimeElement) {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        currentTimeElement.textContent = `${hours}:${minutes}:${seconds}`;
    }
}

export function updateRandomQuote(data) {
    const quoteDiv = document.getElementById('quote');
    if (quoteDiv) {
        quoteDiv.innerHTML = `
            <div>${data.quote.content} - ${data.quote.author}</div>
            <div class="timestamp">Quote updated at: ${data.timestamp}</div>
        `;
    }
}

export function updateRescueTimeData(data) {
    const rescueTimeDiv = document.getElementById('rescuetime_data');
    if (rescueTimeDiv && data.rescuetime_data && data.rescuetime_data.ag) {
        const agData = data.rescuetime_data.ag;
        rescueTimeDiv.innerHTML = `
            <span>Arvy's Screen Time for ${agData.date}:</span><br>
            <span>Productive: ${agData.all_productive_duration_formatted}</span><br>
            <span>Distracting: ${agData.all_distracting_duration_formatted}</span><br>
            <span>Total Time: ${agData.total_duration_formatted}</span><br>
            <span class="timestamp">Screen time updated at: ${data.fetch_date}</span>
        `;
    } else {
        rescueTimeDiv.innerHTML = '<span>RescueTime data not available</span>';
    }
}

export function loadWeatherWidgets() {
    // Load the weather widget script
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
}

export function refreshWeatherWidgets() {
    if (window.__weatherwidget_init) {
        window.__weatherwidget_init();
    }
    
    const weatherContainer = document.querySelector('.weather-widget');
    if (weatherContainer) {
        let weatherTimestampElement = document.getElementById('weather-timestamp');
        if (!weatherTimestampElement) {
            weatherTimestampElement = document.createElement('div');
            weatherTimestampElement.id = 'weather-timestamp';
            weatherTimestampElement.className = 'timestamp';
            weatherContainer.appendChild(weatherTimestampElement);
        }

        const currentTimeElement = document.createElement('span');
        currentTimeElement.id = 'weather-current-time';
        weatherTimestampElement.textContent = 'Weather updated at: ';
        weatherTimestampElement.appendChild(currentTimeElement);
        
        // Use the existing updateCurrentTime function
        const updateWeatherTimestamp = () => {
            updateCurrentTime();
            currentTimeElement.textContent = document.getElementById('current-time').textContent;
        };
        
        updateWeatherTimestamp();
    }
}
