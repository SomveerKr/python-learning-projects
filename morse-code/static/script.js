let currentMode = 'encode';

// Mode selector buttons
const modeBtns = document.querySelectorAll('.mode-btn');
const inputLabel = document.getElementById('inputLabel');
const inputText = document.getElementById('inputText');
const convertBtn = document.getElementById('convertBtn');
const output = document.getElementById('output');
const copyBtn = document.getElementById('copyBtn');

// Mode switching
modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        modeBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentMode = btn.dataset.mode;

        // Update UI based on mode
        if (currentMode === 'encode') {
            inputLabel.textContent = 'Enter Text:';
            inputText.placeholder = 'Type your message here...';
        } else {
            inputLabel.textContent = 'Enter Morse Code:';
            inputText.placeholder = 'Enter morse code (e.g., .... . .-.. .-.. --- / .-- --- .-. .-.. -..)';
        }

        // Clear input and output
        inputText.value = '';
        output.innerHTML = '<span class="placeholder-text">Your converted text will appear here...</span>';
        copyBtn.style.display = 'none';
    });
});

// Convert button
convertBtn.addEventListener('click', async () => {
    const text = inputText.value.trim();

    if (!text) {
        output.innerHTML = '<span class="placeholder-text" style="color: #f5576c;">Please enter some text to convert!</span>';
        copyBtn.style.display = 'none';
        return;
    }

    // Add loading state
    convertBtn.innerHTML = '<span class="btn-text">Converting...</span>';
    convertBtn.disabled = true;

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                mode: currentMode
            })
        });

        const data = await response.json();

        // Display result
        output.textContent = data.result;
        copyBtn.style.display = 'flex';

        // Add success animation
        output.style.animation = 'none';
        setTimeout(() => {
            output.style.animation = 'fadeIn 0.5s ease';
        }, 10);

    } catch (error) {
        output.innerHTML = '<span class="placeholder-text" style="color: #f5576c;">Error converting text. Please try again.</span>';
        copyBtn.style.display = 'none';
    } finally {
        // Reset button
        convertBtn.innerHTML = '<span class="btn-text">Convert</span><span class="btn-icon">→</span>';
        convertBtn.disabled = false;
    }
});

// Copy button
copyBtn.addEventListener('click', async () => {
    const textToCopy = output.textContent;

    try {
        await navigator.clipboard.writeText(textToCopy);

        // Visual feedback
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<span class="copy-icon">✓</span> Copied!';
        copyBtn.style.background = 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)';

        setTimeout(() => {
            copyBtn.innerHTML = originalText;
            copyBtn.style.background = '';
        }, 2000);
    } catch (error) {
        console.error('Failed to copy:', error);
    }
});

// Allow Enter key to convert (with Shift+Enter for new line)
inputText.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        convertBtn.click();
    }
});
