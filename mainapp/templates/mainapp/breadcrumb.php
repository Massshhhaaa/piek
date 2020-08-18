<div id="tp-breadcrumb" class="tp-breadcrumb">
	<div class="container">
		<div class="row">
			<div class="col-md-8">
				<ol class="breadcrumb">
					<?php if ($childpage) : ?>
						<li><a href="/index.php">Главная</a></li>
						<li><a href="/catalog"><?= $thispage ?></a></li>
						<li class="active"><?= $childpage ?></li>
					<?php else : ?>
						<li><a href="/index.php">Главная</a></li>
						<li class="active"><?= $thispage ?></li>
					<?php endif; ?>
				</ol>
			</div>
			<div class="col-md-4 text-right">
				<? require (__DIR__.'/../../phprusearch/sinc/form.php') ?>
			</div>
		</div>
	</div>
</div>