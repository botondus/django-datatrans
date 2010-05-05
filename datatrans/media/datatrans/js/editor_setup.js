tinyMCE.init({
	mode : "none",
	theme : "simple",
});

function toggleEditor(id) {
	if (!tinyMCE.get(id)) {
		tinyMCE.execCommand('mceAddControl', false, id);
	}
	else {
		tinyMCE.execCommand('mceFocus', false, id); 
		tinyMCE.execCommand('mceRemoveControl', false, id);
	}
}