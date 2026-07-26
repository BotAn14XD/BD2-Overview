---

description:
comments: false
image: assets/images/site-assets/survey-banner.png
icon: material/poll

---
![Survey](assets/images/site-assets/index-pc-nav-22.avif){: .card-header-img }

#



<form id="custom-survey">
  
<p>What is your nickname? (Optional)</p>
<textarea name="nickname" rows="1" placeholder="Your nickname..."></textarea>

<hr>

<p>Where did you first hear about the Compendium?</p>
<label class="survey-choice-box"><input type="radio" name="source" value="Discord" required>Discord</label>
<label class="survey-choice-box"><input type="radio" name="source" value="Web Search">Web Search</label>
<label class="survey-choice-box"><input type="radio" name="source" value="Reddit">Reddit</label>
<label class="survey-choice-box"><input type="radio" name="source" value="Souseha's Database">Souseha's Database</label>
<label class="survey-choice-box"><input type="radio" name="source" value="Miraheze Wiki">Miraheze Wiki</label>
<label class="survey-choice-box">
<div class="survey-choice-other-wrapper">
    <input type="radio" name="source" value="Other" id="other-radio-source">
    <span>Other:</span>
    <input type="text" id="other-text-source" placeholder="Please specify..." disabled>
</div>
</label>

<hr>

<p>Rate the quality and usefulness of the Compendium's content.</p>
<span class="subtext-label">(5 — Excellent, 1 — Very poor)</span>
<div class="rating-row">
<label class="rating-cell"><input type="radio" name="content" value="5" required>5</label>
<label class="rating-cell"><input type="radio" name="content" value="4">4</label>
<label class="rating-cell"><input type="radio" name="content" value="3">3</label>
<label class="rating-cell"><input type="radio" name="content" value="2">2</label>
<label class="rating-cell"><input type="radio" name="content" value="1">1</label>
</div>

<p>Do you have any suggestions or thoughts regarding our content? (Optional)</p>
<textarea name="content_thoughts" rows="3" placeholder="Share your feedback on guides, mechanics write-ups, etc..."></textarea>

<hr>

<p>How easy is it to navigate and find information on the Compendium?</p>
<span class="subtext-label">(5 — Very easy, 1 — Very frustrating)</span>
<div class="rating-row">
<label class="rating-cell"><input type="radio" name="accessibility" value="5" required>5</label>
<label class="rating-cell"><input type="radio" name="accessibility" value="4">4</label>
<label class="rating-cell"><input type="radio" name="accessibility" value="3">3</label>
<label class="rating-cell"><input type="radio" name="accessibility" value="2">2</label>
<label class="rating-cell"><input type="radio" name="accessibility" value="1">1</label>
</div>

<p>Do you have any suggestions or thoughts regarding the navigation? (Optional)</p>
<textarea name="accessibility_thoughts" rows="3" placeholder="Share your feedback regarding navigation..."></textarea>

<hr>

<p>How comfortable is the Compendium to read? (Font size, contrast, colors, mobile layout)</p>
<span class="subtext-label">(5 — Perfect, 1 — Hard on the eyes)</span>
<div class="rating-row">
  <label class="rating-cell"><input type="radio" name="readability" value="5" required>5</label>
  <label class="rating-cell"><input type="radio" name="readability" value="4">4</label>
  <label class="rating-cell"><input type="radio" name="readability" value="3">3</label>
  <label class="rating-cell"><input type="radio" name="readability" value="2">2</label>
  <label class="rating-cell"><input type="radio" name="readability" value="1">1</label>
</div>

<p>Do you have any suggestions or thoughts regarding the visual readability? (Optional)</p>
<textarea name="readability_thoughts" rows="3" placeholder="Share your feedback regarding visual readability..."></textarea>

<hr>

<p>Rate the quality of the Compendium's <b>text</b>.</p>
<span class="subtext-label">(5 — Excellent, 1 — Very poor)</span>
<div class="rating-row">
<label class="rating-cell"><input type="radio" name="text" value="5" required>5</label>
<label class="rating-cell"><input type="radio" name="text" value="4">4</label>
<label class="rating-cell"><input type="radio" name="text" value="3">3</label>
<label class="rating-cell"><input type="radio" name="text" value="2">2</label>
<label class="rating-cell"><input type="radio" name="text" value="1">1</label>
</div>

<p>Do you have any suggestions or thoughts regarding the quality of the text? (Optional)</p>
<textarea name="text_thoughts" rows="3" placeholder="Share your feedback regarding the text quality..."></textarea>

<hr>

<p>Name <b>one</b> Article that is, in your opinion, the best.</p>
<textarea name="best_article" rows="1" placeholder="Gear System..."></textarea>

<p>Name <b>one</b> Article that is, in your opinion, the worst.</p>
<textarea name="worst_article" rows="1" placeholder="Mirror Wars..."></textarea>

<p>Name <b>one</b> Topic / Article that is missing and you want to see the most.</p>
<textarea name="awaiting_stuff" rows="1" placeholder="The Soul Wager..."></textarea>

<hr>

<p>Do you support the introduction of unobtrusive ads?</p>
<label class="survey-choice-box"><input type="radio" name="ads" value="Yes" required>Yes</label>
<label class="survey-choice-box"><input type="radio" name="ads" value="No">No</label>
<label class="survey-choice-box"><input type="radio" name="ads" value="No Preference">No Preference / Whatever</label>

<p>If there were a Patreon subscription, would you pay for it, and if yes, is there anything you would like to have as a "reward" for a subscription?</p>

<label class="survey-choice-box">
<div class="survey-choice-other-wrapper">
    <input type="radio" name="patreon" value="Other" id="other-radio-patreon" required>
    <span>Yes:</span>
    <input type="text" id="other-text-patreon" placeholder="Please specify..." disabled>
</div></label>
<label class="survey-choice-box"><input type="radio" name="patreon" value="No">No</label>
<label class="survey-choice-box"><input type="radio" name="patreon" value="Not Interested">Not Interested</label>

<hr>

<p>Is there anything else you'd like to share with us? (Optional)</p>
<textarea name="feedback_long" rows="5" placeholder="General comments, feature requests, or bugs..."></textarea>

<hr style="border-top-style: dashed;">

<button type="submit" id="submit-btn">Submit Survey</button>

<div id="status-message"></div>

</form>


<script>
  const form = document.getElementById('custom-survey');
  const btn = document.getElementById('submit-btn');
  const statusMessage = document.getElementById('status-message');

  const scriptURL = 'https://script.google.com/macros/s/AKfycbx8DsS4WqvX63SSJB6S1c0hVZxUIhtDRunLWOwsqXRmmozifC1zluuyb5PUXQ70Y6EB/exec';

  form.addEventListener('change', (e) => {
    if (e.target.type === 'radio') {
      const groupName = e.target.name; 
      const otherTextInput = document.getElementById(`other-text-${groupName}`);

      if (otherTextInput) {
        if (e.target.value === 'Other') {
          otherTextInput.disabled = false;
          otherTextInput.required = true;
          otherTextInput.focus();
        } else {
          otherTextInput.disabled = true;
          otherTextInput.required = false;
          otherTextInput.value = '';
        }
      }
    }
  });
  form.addEventListener('submit', e => {
    e.preventDefault();
    btn.disabled = true;
    btn.textContent = "Submitting...";
    const formData = new FormData(form);
    const allOtherInputs = form.querySelectorAll('input[id^="other-text-"]');
    allOtherInputs.forEach(input => {
      const groupName = input.id.replace('other-text-', '');
      if (formData.get(groupName) === 'Other') {
        formData.set(groupName, input.value); 
      }
      input.disabled = true;
    });

    fetch(scriptURL, { method: 'POST', body: formData })
      .then(response => {
        statusMessage.className = 'status-success';
        statusMessage.style.color = "#4ade80"; 
        statusMessage.textContent = "Survey submitted successfully!";
        
        form.reset();
        btn.disabled = false;
        btn.textContent = "Submit Survey";
      })
      .catch(error => {
        console.error('Error!', error.message);

        statusMessage.className = 'status-error';
        statusMessage.style.color = "#f87171"; 
        statusMessage.textContent = "There was an error submitting the survey.";
        
        btn.disabled = false;
        btn.textContent = "Submit Survey";
      });
  });
</script>