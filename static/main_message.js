	const nav_btn = document.querySelector('.nav_btn');
	const msg = document.querySelector('#msg_id');

	const msg_content = document.querySelector('#msg_content');
	const msg_name = document.querySelector('#msg_content');
	const msg_pw = document.querySelector('#msg_content');
	const submit_btn = document.querySelector('#submit_btn');

	const red = document.querySelector('#red');
	const purple = document.querySelector('#purple');
	const orange = document.querySelector('#orange');
	const blue = document.querySelector('#blue');
	const mint = document.querySelector('#mint');
	const skyblue = document.querySelector('#skyblue');

	function goback () {
		const prev_url = location.search
		location.href = `/rolling/guest${prev_url}`;
	}

	nav_btn.addEventListener("click", goback);

	var candle_id = '';

	function sel_candle(candle) {
		// console.log(candle.id);

		// candle_id = e['path'][0]['id'];

		// console.log('first', candle_id);
		// this.style.boxShadow = '0 0 0 0.25rem #FFA3B5';
	}

	red.addEventListener("click", sel_candle(red));
	purple.addEventListener("click", sel_candle(purple));
	orange.addEventListener("click", sel_candle(orange));
	blue.addEventListener("click", sel_candle(blue));
	mint.addEventListener("click", sel_candle(mint));
	skyblue.addEventListener("click", sel_candle(skyblue));

	$('#red').click((e) => candle_id = e.target.id);
	$('#purple').click((e) => candle_id = e.target.id);
	$('#orange').click((e) => candle_id = e.target.id);
	$('#blue').click((e) => candle_id = e.target.id);
	$('#mint').click((e) => candle_id = e.target.id);
	$('#skyblue').click((e) => candle_id = e.target.id);

    $('#msg_content').click(() => console.log(candle_id));
	$('#msg_name').click(() => console.log(candle_id));
	$('#msg_pw').click(() => console.log(candle_id));
	function save_msg() {
			const prev_url = location.search
				location.href = `/rolling/guest${prev_url}`;
			const rolling_num = Number(location.search.split("&")[0].split("=")[1])

            let name = $('#msg_name').val()
            let pwd = $('#msg_pw').val()
            let content = $('#msg_content').val()

			if (candle_id == "") {
				alert("전달할 캔들을 선택해주세요");
			} else if (content == "") {
				alert("메시지를 입력해주세요");
			} else if (name == "") {
				alert("닉네임을 입력해주세요");
			} else if (pwd == "") {
				alert("비밀번호를 입력해주세요");
			} else {
				$.ajax({
                    type: "POST",
                    url: "/message/save_msg",
                    data: {msg_give: content, nick_give: name, pwd_give: pwd, candle_give: candle_id, rolling_give: rolling_num},
                    success: function (response) {
							alert(response['msg']);
							const prev_url = location.search
							window.location.reload();
							location.href = `/rolling/guest/${prev_url}`;


                        }
                    });
			}
	}








