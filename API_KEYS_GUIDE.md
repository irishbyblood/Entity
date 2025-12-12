# How to Get API Keys for Entity

Entity requires API keys from AI providers to function. You need to obtain these keys yourself by signing up with the respective services. Here's how:

## 🔑 Required API Keys

You need **at least one** of the following API keys for Entity to work:

### 1. OpenAI API Key (Recommended)
**Provides**: GPT-4 (Creative Cortex) + DALL-E 3 (Visual Cortex)

**How to get it:**
1. Go to [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. Create an account or sign in
3. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key (starts with `sk-...`)
6. **Important**: Store it securely - you can only see it once!

**Cost**: Pay-as-you-go pricing
- GPT-4: ~$0.03 per 1K tokens (input) / $0.06 per 1K tokens (output)
- DALL-E 3: ~$0.040 per image (1024x1024)
- Free trial credits available for new users

**Documentation**: [https://platform.openai.com/docs](https://platform.openai.com/docs)

---

### 2. Anthropic API Key (Optional but Recommended)
**Provides**: Claude 3.5 Sonnet (Logic Cortex)

**How to get it:**
1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up for an account
3. Navigate to API Keys section
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-...`)

**Cost**: Pay-as-you-go pricing
- Claude 3.5 Sonnet: ~$0.003 per 1K tokens (input) / $0.015 per 1K tokens (output)
- Free trial credits available

**Documentation**: [https://docs.anthropic.com/](https://docs.anthropic.com/)

---

### 3. Google Gemini API Key (Optional - Fallback)
**Provides**: Gemini Pro (Fallback for Creative/Logic Cortex)

**How to get it:**
1. Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

**Cost**: 
- Free tier available with generous limits
- Pay-as-you-go for higher usage

**Documentation**: [https://ai.google.dev/docs](https://ai.google.dev/docs)

---

## ⚙️ Setting Up Your Keys

### Step 1: Copy the Example File
```bash
cd Entity
cp .env.example .env
```

### Step 2: Edit the .env File
Open `.env` in a text editor:
```bash
nano .env
# or
code .env
# or use any text editor
```

### Step 3: Add Your Keys
Replace the placeholder values with your actual API keys:

```env
# OpenAI API Key (for GPT-4 and DALL-E 3)
OPENAI_API_KEY=sk-proj-abcdef123456...your-actual-key-here

# Anthropic API Key (for Claude 3.5 Sonnet)
ANTHROPIC_API_KEY=sk-ant-api03-xyz789...your-actual-key-here

# Google Gemini API Key (optional)
GEMINI_API_KEY=AIzaSy...your-actual-key-here

# Generate a secure secret key
SECRET_KEY=your-generated-secret-key-here
```

### Step 4: Generate a Secret Key
Run this command to generate a secure SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it as your SECRET_KEY in the `.env` file.

### Step 5: Save and Start Entity
Save the `.env` file and start Entity:
```bash
./start.sh
```

---

## 🎯 Minimum Requirements

**To run Entity, you need at least ONE of these configurations:**

### Option 1: OpenAI Only (Recommended for Beginners)
```env
OPENAI_API_KEY=sk-...
```
- ✅ Visual Cortex (DALL-E 3)
- ✅ Creative Cortex (GPT-4)
- ⚠️ Logic Cortex will fallback to GPT-4
- ⚠️ Memory Cortex works (no API key needed)

### Option 2: OpenAI + Anthropic (Best Experience)
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```
- ✅ All cortexes fully functional
- ✅ Best reasoning with Claude
- ✅ Best creativity with GPT-4
- ✅ Image generation with DALL-E 3

### Option 3: Anthropic + Gemini (Budget Option)
```env
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...
```
- ✅ Logic Cortex (Claude)
- ✅ Creative Cortex fallback (Gemini)
- ❌ No image generation (Visual Cortex unavailable)

---

## 💰 Cost Estimates

**Light Usage** (100 messages/day):
- OpenAI only: ~$5-10/month
- OpenAI + Anthropic: ~$8-15/month
- With images: Add ~$2-5/month

**Moderate Usage** (500 messages/day):
- OpenAI only: ~$20-40/month
- OpenAI + Anthropic: ~$30-60/month

**Tips to Reduce Costs:**
1. Use Gemini (free tier) as fallback
2. Limit image generation (DALL-E is more expensive)
3. Use Claude for code/analysis (cheaper than GPT-4)
4. Monitor usage in provider dashboards

---

## 🔒 Security Best Practices

### ✅ DO:
- Store API keys in `.env` file (not in code)
- Add `.env` to `.gitignore` (already done)
- Rotate keys periodically
- Set spending limits in provider dashboards
- Monitor usage regularly

### ❌ DON'T:
- Commit `.env` to Git
- Share your API keys
- Use keys in public repositories
- Use production keys for testing
- Ignore usage alerts

---

## 🧪 Testing Your Setup

After adding your keys, test Entity:

```bash
# Start the backend
python api.py
```

In another terminal:
```bash
# Test the API
curl http://localhost:8000/status
```

You should see which cortexes are available:
```json
{
  "name": "Entity",
  "cortexes": {
    "visual": true,    // if OpenAI key is valid
    "logic": true,     // if Anthropic key is valid
    "creative": true,  // if OpenAI or Gemini key is valid
    "memory": true     // always true (no key needed)
  }
}
```

---

## ❓ Troubleshooting

### "Invalid API key" Error

**For OpenAI:**
- Verify key starts with `sk-`
- Check key hasn't expired
- Ensure you have credits: [https://platform.openai.com/account/usage](https://platform.openai.com/account/usage)

**For Anthropic:**
- Verify key starts with `sk-ant-`
- Check if API access is enabled in your account
- Verify billing is set up: [https://console.anthropic.com/](https://console.anthropic.com/)

**For Gemini:**
- Verify key format
- Check if API is enabled in Google Cloud Console
- Ensure you haven't exceeded free tier limits

### "Cortex unavailable" Message

This is normal if:
- You haven't provided that specific API key
- Entity will use fallback models automatically
- Memory Cortex always works (no key needed)

### Environment Variables Not Loading

1. Make sure `.env` file is in the root directory
2. Restart the API server after changing `.env`
3. Check for spaces or quotes around values (should be: `KEY=value` not `KEY="value"`)

---

## 📞 Getting Help

**For API Key Issues:**
- OpenAI Support: [https://help.openai.com/](https://help.openai.com/)
- Anthropic Support: [https://support.anthropic.com/](https://support.anthropic.com/)
- Google AI Support: [https://support.google.com/](https://support.google.com/)

**For Entity Issues:**
- Check SETUP.md for installation issues
- Review README.md for configuration
- Open an issue on GitHub

---

## 📝 Summary Checklist

- [ ] Sign up for OpenAI account
- [ ] Create OpenAI API key
- [ ] (Optional) Sign up for Anthropic
- [ ] (Optional) Create Anthropic API key
- [ ] (Optional) Get Google Gemini key
- [ ] Copy `.env.example` to `.env`
- [ ] Add your API keys to `.env`
- [ ] Generate and add SECRET_KEY
- [ ] Save `.env` file
- [ ] Test with `python api.py`
- [ ] Verify cortexes are available
- [ ] Start using Entity!

---

**Note**: API keys are personal credentials. Never share them or commit them to version control. Entity has been configured to keep your keys secure in the `.env` file.

**Ready to start?** Follow the steps above to get your keys, then run `./start.sh` to launch Entity! 🚀
