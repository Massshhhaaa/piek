<div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				<h4 class="modal-title" id="myModalLabel">Заказать товар</h4>
			</div>
			<div class="modal-body">
				<div class="row">
					<form method="post" id="contactform">	
						<div class="col-md-12">
							<h4>Наименование товара:</h4>
							<input class="form-control input-md tovarhere" name="tovar" />
						</div>
						<div class="form-group">
							<div class="col-md-6">
								<label class="control-label">Контактное лицо*</label>
								<input class="form-control input-md" maxlength="255" size="45" id="name" name="name" />
							</div>
						</div>
						
						<div class="form-group">
							<div class="col-md-6">
								<label class="control-label">Количество*</label>
								<input class="form-control input-md" maxlength="255" size="45" id="colvo" name="colvo" />
							</div>
						</div>
						
						<div class="form-group">
							<div class="col-md-6">
								<label class="control-label">ваш E-mail*</label>
								<input class="form-control input-md" maxlength="255" size="45" id="email" name="email" />
							</div>
						</div>
						
						<div class="form-group">
							<div class="col-md-12">
								<label class="control-label">Введите текст письма*</label>
								<textarea class="form-control" onkeypress=" if (this.value.length &gt;= 100000 ) return false" name="comment" rows="7" cols="53"></textarea>
							</div>
						</div>
						
						<div class="form-group">
							<div class="col-md-12">
								<div id="alert"></div>
							</div>
						</div>
						
						<div class="col-md-12">
							<input class="btn tp-btn-yellow tp-btn-rounded" id="submit" type="submit" value="Отправить" name="btn_submit" />
							<input class="btn tp-btn-yellow tp-btn-rounded" type="reset" value="Сброс" name="B2" />
						</div>
					</form>
				</div>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" data-dismiss="modal">Закрыть</button>
			</div>
		</div>
	</div>
</div>

<script>
	$(document).ready(function(){
		$('button.btn-primary').click(function(){
			console.log($(this).attr('name'));
			$('.tovarhere').val($(this).attr('name'));
			
		})

		
		$('input#submit').click(function(){
			var dataString = $('#contactform').serialize();
			var a = $('input#name').val()
			var b = $('input#email').val()
			var c = $('input#colvo').val()
			var d = $('input#comment').val()
			console.info('okay');
			if (a != '' ) {
				if (b != '') {
					if (c != '') {
						$.ajax({
							type: "POST",
							url: "/contact/mail2.php",
							data: dataString,
							success: function () {
								$('#alert').prepend("<div class=\"alert alert-success fade in\"><button class=\"close\" data-dismiss=\"alert\" type=\"button\">&times;</button><strong>Сообщение успешно отправлено!</strong> Мы свяжемся с вами в ближайшее время.</div>");
								$('#contactform')[0].reset();
								console.info('отправлено');
							},
							error: function(response) {
								console.log('ошибка');
							}
						});
					}
				}
			} else {
				$('#alert').prepend("<div class=\"alert alert-warning fade in\"><button class=\"close\" data-dismiss=\"alert\" type=\"button\">&times;</button><strong>Ошибка!</strong> Заполните поля.</div>");
			}
			
			if (a == '') {
				$('input#name').addClass('vlred');
			} else {
				$('input#name').removeClass('vlred');
			}
			
			if (b == '') {
				$('input#email').addClass('vlred');
			} else {
				$('input#email').removeClass('vlred');
			}
			
			if (c == '') {
				$('input#colvo').addClass('vlred');
			} else {
				$('input#colvo').removeClass('vlred');
			}
			
			if (d == '') {
				$('input#comment').addClass('vlred');
			} else {
				$('input#comment').removeClass('vlred');
			}
			
		})
		
	})
</script>