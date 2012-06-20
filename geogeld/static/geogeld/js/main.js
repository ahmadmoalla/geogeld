$ = jQuery;


function chose_category(){
	$button = $(this);
	$('.job-category-button').removeClass('chosen');
	$button.addClass('chosen');
	
	$('#job-category').val($button.attr('cat-name'));
}

function toggle_job_title_state(){
	$title_text_box = $(this);
	console.log($title_text_box);
	if ($title_text_box.is(':focus')){
		if ($title_text_box.val() == 'Title'){
			$title_text_box.val('');
		}
		
	} else {
		if ($title_text_box.val().length == 0){
			$title_text_box.val('Title');
		}
		
	}
}

$('.job-category-button').live('click', chose_category);
//$('#job-title').live('click', toggle_job_title_state);
//$('#job-title').live('blur', toggle_job_title_state);
