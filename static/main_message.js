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

	let candle_id = '';

	function sel_candle(e) {
		candle_id = e['path'][0]['id'];
		console.log('first', candle_id);
		/*
		if (candle_id == 'candle_1') {
			candle_id = red;
		} else if (candle_id == 'candle_2') {
			candle_id = purple;
		} else if (candle_id == 'candle_3') {
			candle_id = orange;
		} else if (candle_id == 'candle_4') {
			candle_id = blue;
		} else if (candle_id == 'candle_5') {
			candle_id = mint;
		} else if (candle_id == 'candle_6') {
			candle_id = skyblue;
			console.log('middle', candle_id);
		}
		 */

	}

	red.addEventListener("click", sel_candle);
	purple.addEventListener("click", sel_candle);
	orange.addEventListener("click", sel_candle);
	blue.addEventListener("click", sel_candle);
	mint.addEventListener("click", sel_candle);
	skyblue.addEventListener("click", sel_candle);

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








