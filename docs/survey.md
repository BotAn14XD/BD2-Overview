<form id="custom-survey">
  
  <p>What is your nickname (Optional)?</p>
  <textarea name="nickname" rows="1" placeholder="Your nickname..."></textarea>

  <hr>

  <p>Where did you first hear about Compendium?</p>
  <label class="survey-choice-box"><input type="radio" name="source" value="Discord" required>Discord</label>
  <label class="survey-choice-box"><input type="radio" name="source" value="Web Search">Web Search</label>
  <label class="survey-choice-box"><input type="radio" name="source" value="Reddit">Reddit</label>
  <label class="survey-choice-box"><input type="radio" name="source" value="Souseha's Database">Souseha's Database</label>
  <label class="survey-choice-box"><input type="radio" name="source" value="Miraheze Wiki">Miraheze Wiki</label>
  <label class="survey-choice-box">
    <div class="survey-choice-other-wrapper">
      <input type="radio" name="source" value="Other" id="source-other-radio">
      <span>Other:</span>
      <input type="text" id="source-other-text" placeholder="Please specify..." disabled>
    </div>
  </label>

  <hr>

  <p>Rate the quality and usefulness of Compendium's content</p>
  <span class="subtext-label">(5 — Excellent, 1 — Very poor)</span>
  <div class="rating-row">
    <label class="rating-cell"><input type="radio" name="content" value="5" required>5</label>
    <label class="rating-cell"><input type="radio" name="content" value="4">4</label>
    <label class="rating-cell"><input type="radio" name="content" value="3">3</label>
    <label class="rating-cell"><input type="radio" name="content" value="2">2</label>
    <label class="rating-cell"><input type="radio" name="content" value="1">1</label>
  </div>

  <p>Do you have any suggestions or thoughts regarding our content?</p>
  <textarea name="content_thoughts" rows="3" placeholder="Share your feedback on guides, mechanics writeups etc..."></textarea>

  <hr>

  <p>How easy is it to navigate and find information on Compendium?</p>
  <span class="subtext-label">(5 — Very easy, 1 — Very frustrating)</span>
  <div class="rating-row">
    <label class="rating-cell"><input type="radio" name="accessibility" value="5" required>5</label>
    <label class="rating-cell"><input type="radio" name="accessibility" value="4">4</label>
    <label class="rating-cell"><input type="radio" name="accessibility" value="3">3</label>
    <label class="rating-cell"><input type="radio" name="accessibility" value="2">2</label>
    <label class="rating-cell"><input type="radio" name="accessibility" value="1">1</label>
  </div>

  <p>Do you have any suggestions or thoughts regarding the navigation?</p>
  <textarea name="accessibility_thoughts" rows="3" placeholder="Share your feedback navigation..."></textarea>

  <hr>

  <p>Is there anything else you'd like to share with us? (Optional)</p>
  <textarea name="feedback_long" rows="3" placeholder="General comments, feature requests, or bugs..."></textarea>

  <hr style="border-top-style: dashed;">

  <button type="submit" id="submit-btn">Submit Survey</button>
  <div id="status-message"></div>

</form>


<script>
  const form = document.getElementById('custom-survey');
  const btn = document.getElementById('submit-btn');
  const statusMessage = document.getElementById('status-message');
  const sourceRadios = document.querySelectorAll('input[name="source"]');
  const sourceOtherText = document.getElementById('source-other-text');


  const scriptURL = 'https://script.google.com/macros/s/AKfycbx8DsS4WqvX63SSJB6S1c0hVZxUIhtDRunLWOwsqXRmmozifC1zluuyb5PUXQ70Y6EB/exec';

  
  sourceRadios.forEach(radio => {
  radio.addEventListener('change', (e) => {
    if (e.target.value === 'Other') {
      sourceOtherText.disabled = false;
      sourceOtherText.required = true; 
      sourceOtherText.focus();
    } else {
      sourceOtherText.disabled = true;
      sourceOtherText.required = false;
      sourceOtherText.value = ''; 
    }
  });
  });

  form.addEventListener('submit', e => {
  e.preventDefault();
  
  btn.disabled = true;
  btn.textContent = "Submitting...";

  const formData = new FormData(form);

  if (formData.get('source') === 'Other') {
    formData.set('source', sourceOtherText.value);
  }

  fetch(scriptURL, { method: 'POST', body: formData })
    .then(response => {
      statusMessage.textContent = "Survey submitted successfully!";
      form.reset();

      sourceOtherText.disabled = true; 
      btn.disabled = false;
      btn.textContent = "Submit Survey";
    })
    .catch(error => {
      console.error('Error!', error.message);
    });
});

</script>