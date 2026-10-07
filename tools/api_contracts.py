"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = "/kling/tasks"

ENDPOINTS = {
    "kling_generate_video": {
        "method": "POST",
        "path": "/kling/videos",
        "operation": "generate",
        "schema": {
            "type": "object",
            "required": ["action"],
            "properties": {
                "mode": {"enum": ["std", "pro", "4k"], "type": "string"},
                "model": {
                    "enum": [
                        "kling-v3-turbo",
                        "kling-v1",
                        "kling-v1-6",
                        "kling-v2-master",
                        "kling-v2-1-master",
                        "kling-v2-5-turbo",
                        "kling-v2-6",
                        "kling-v3",
                        "kling-v3-omni",
                        "kling-o1",
                    ],
                    "type": "string",
                },
                "action": {"enum": ["text2video", "image2video", "extend"], "type": "string"},
                "prompt": {"type": "string"},
                "duration": {"type": "number"},
                "generate_audio": {"type": "boolean"},
                "video_id": {"type": "string"},
                "cfg_scale": {"type": "number", "minimum": 0, "maximum": 1},
                "aspect_ratio": {"enum": ["16:9", "9:16", "1:1"], "type": "string"},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
                "end_image_url": {"type": "string"},
                "camera_control": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": [
                                "simple",
                                "down_back",
                                "forward_up",
                                "left_turn_forward",
                                "right_turn_forward",
                            ],
                        },
                        "config": {
                            "type": "object",
                            "additionalProperties": {"type": "number", "minimum": -1, "maximum": 1},
                            "properties": {},
                        },
                    },
                },
                "image_list": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 7,
                    "items": {
                        "type": "object",
                        "required": ["image_url"],
                        "properties": {
                            "image_url": {"type": "string", "format": "uri"},
                            "type": {"type": "string", "enum": ["first_frame", "end_frame"]},
                        },
                    },
                },
                "video_list": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 1,
                    "items": {
                        "type": "object",
                        "required": ["video_url"],
                        "properties": {
                            "video_url": {"type": "string", "format": "uri"},
                            "refer_type": {"type": "string", "enum": ["base", "feature"]},
                            "keep_original_sound": {"type": "string", "enum": ["yes", "no"]},
                        },
                    },
                },
                "negative_prompt": {"type": "string"},
                "start_image_url": {"type": "string"},
                "multi_shot": {"type": "boolean"},
                "shot_type": {"type": "string", "enum": ["customize", "intelligence"]},
                "multi_prompt": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 6,
                    "items": {
                        "type": "object",
                        "required": ["index", "prompt", "duration"],
                        "properties": {
                            "index": {"type": "integer", "minimum": 1, "maximum": 6},
                            "prompt": {"type": "string", "minLength": 1, "maxLength": 512},
                            "duration": {"type": "integer", "minimum": 1, "maximum": 15},
                        },
                    },
                },
                "element_list": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 3,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["element_id"],
                        "properties": {"element_id": {"type": "string", "minLength": 1}},
                    },
                },
                "voice_list": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 2,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["voice_id"],
                        "properties": {"voice_id": {"type": "string", "minLength": 1}},
                    },
                },
            },
            "anyOf": [
                {"required": ["prompt"]},
                {
                    "required": ["multi_shot", "shot_type", "multi_prompt"],
                    "properties": {
                        "multi_shot": {"enum": [True]},
                        "shot_type": {"enum": ["customize"]},
                    },
                },
            ],
        },
        "properties": {
            "mode": {"enum": ["std", "pro", "4k"], "type": "string"},
            "model": {
                "enum": [
                    "kling-v3-turbo",
                    "kling-v1",
                    "kling-v1-6",
                    "kling-v2-master",
                    "kling-v2-1-master",
                    "kling-v2-5-turbo",
                    "kling-v2-6",
                    "kling-v3",
                    "kling-v3-omni",
                    "kling-o1",
                ],
                "type": "string",
            },
            "action": {"enum": ["text2video", "image2video", "extend"], "type": "string"},
            "prompt": {"type": "string"},
            "duration": {"type": "number"},
            "generate_audio": {"type": "boolean"},
            "video_id": {"type": "string"},
            "cfg_scale": {"type": "number", "minimum": 0, "maximum": 1},
            "aspect_ratio": {"enum": ["16:9", "9:16", "1:1"], "type": "string"},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
            "end_image_url": {"type": "string"},
            "camera_control": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "simple",
                            "down_back",
                            "forward_up",
                            "left_turn_forward",
                            "right_turn_forward",
                        ],
                    },
                    "config": {
                        "type": "object",
                        "additionalProperties": {"type": "number", "minimum": -1, "maximum": 1},
                        "properties": {},
                    },
                },
            },
            "image_list": {
                "type": "array",
                "minItems": 1,
                "maxItems": 7,
                "items": {
                    "type": "object",
                    "required": ["image_url"],
                    "properties": {
                        "image_url": {"type": "string", "format": "uri"},
                        "type": {"type": "string", "enum": ["first_frame", "end_frame"]},
                    },
                },
            },
            "video_list": {
                "type": "array",
                "minItems": 1,
                "maxItems": 1,
                "items": {
                    "type": "object",
                    "required": ["video_url"],
                    "properties": {
                        "video_url": {"type": "string", "format": "uri"},
                        "refer_type": {"type": "string", "enum": ["base", "feature"]},
                        "keep_original_sound": {"type": "string", "enum": ["yes", "no"]},
                    },
                },
            },
            "negative_prompt": {"type": "string"},
            "start_image_url": {"type": "string"},
            "multi_shot": {"anyOf": [{"type": "boolean"}, {"enum": [True]}]},
            "shot_type": {"type": "string", "enum": ["customize", "intelligence"]},
            "multi_prompt": {
                "type": "array",
                "minItems": 1,
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "required": ["index", "prompt", "duration"],
                    "properties": {
                        "index": {"type": "integer", "minimum": 1, "maximum": 6},
                        "prompt": {"type": "string", "minLength": 1, "maxLength": 512},
                        "duration": {"type": "integer", "minimum": 1, "maximum": 15},
                    },
                },
            },
            "element_list": {
                "type": "array",
                "minItems": 1,
                "maxItems": 3,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["element_id"],
                    "properties": {"element_id": {"type": "string", "minLength": 1}},
                },
            },
            "voice_list": {
                "type": "array",
                "minItems": 1,
                "maxItems": 2,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["voice_id"],
                    "properties": {"voice_id": {"type": "string", "minLength": 1}},
                },
            },
        },
        "parameters": [],
        "defaults": {
            "model": "kling-v3-turbo",
            "action": "text2video",
            "mode": "std",
            "duration": 5,
            "aspect_ratio": "16:9",
        },
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_generate_motion": {
        "method": "POST",
        "path": "/kling/motion",
        "operation": "request",
        "schema": {
            "type": "object",
            "required": ["image_url", "video_url", "character_orientation", "mode"],
            "properties": {
                "model_name": {"enum": ["kling-v2-6", "kling-v3"], "type": "string"},
                "mode": {"enum": ["std", "pro"], "type": "string"},
                "keep_original_sound": {"enum": ["yes", "no"], "type": "string"},
                "watermark_info": {
                    "type": "object",
                    "properties": {"enabled": {"type": "boolean"}},
                },
                "image_url": {"type": "string", "format": "uri"},
                "video_url": {"type": "string", "format": "uri"},
                "character_orientation": {"enum": ["image", "video"], "type": "string"},
                "prompt": {"type": "string"},
                "callback_url": {"type": "string", "format": "uri"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "model_name": {"enum": ["kling-v2-6", "kling-v3"], "type": "string"},
            "mode": {"enum": ["std", "pro"], "type": "string"},
            "keep_original_sound": {"enum": ["yes", "no"], "type": "string"},
            "watermark_info": {"type": "object", "properties": {"enabled": {"type": "boolean"}}},
            "image_url": {"type": "string", "format": "uri"},
            "video_url": {"type": "string", "format": "uri"},
            "character_orientation": {"enum": ["image", "video"], "type": "string"},
            "prompt": {"type": "string"},
            "callback_url": {"type": "string", "format": "uri"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_lip_sync": {
        "method": "POST",
        "path": "/kling/lip-sync",
        "operation": "request",
        "schema": {
            "type": "object",
            "required": ["mode"],
            "properties": {
                "video_id": {"type": "string"},
                "video_url": {"type": "string", "format": "uri"},
                "mode": {"type": "string", "enum": ["audio2video", "text2video"]},
                "audio_url": {"type": "string", "format": "uri"},
                "audio_type": {"type": "string", "enum": ["url", "file"]},
                "audio_file": {"type": "string"},
                "text": {"type": "string", "maxLength": 120},
                "voice_id": {"type": "string"},
                "voice_language": {"type": "string", "enum": ["zh", "en"]},
                "voice_speed": {"type": "number", "minimum": 0.8, "maximum": 2.0},
                "callback_url": {"type": "string", "format": "uri"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "video_id": {"type": "string"},
            "video_url": {"type": "string", "format": "uri"},
            "mode": {"type": "string", "enum": ["audio2video", "text2video"]},
            "audio_url": {"type": "string", "format": "uri"},
            "audio_type": {"type": "string", "enum": ["url", "file"]},
            "audio_file": {"type": "string"},
            "text": {"type": "string", "maxLength": 120},
            "voice_id": {"type": "string"},
            "voice_language": {"type": "string", "enum": ["zh", "en"]},
            "voice_speed": {"type": "number", "minimum": 0.8, "maximum": 2.0},
            "callback_url": {"type": "string", "format": "uri"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_talking_photo": {
        "method": "POST",
        "path": "/kling/talking-photo",
        "operation": "request",
        "schema": {
            "type": "object",
            "required": ["image_url", "audio_url"],
            "properties": {
                "image_url": {"type": "string", "format": "uri"},
                "audio_url": {"type": "string", "format": "uri"},
                "prompt": {"type": "string"},
                "model": {
                    "type": "string",
                    "enum": [
                        "kling-v1",
                        "kling-v1-6",
                        "kling-v2-master",
                        "kling-v2-1-master",
                        "kling-v2-5-turbo",
                        "kling-v2-6",
                    ],
                },
                "duration": {"type": "integer", "enum": [5, 10]},
                "mode": {"type": "string", "enum": ["std", "pro"]},
                "callback_url": {"type": "string", "format": "uri"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "image_url": {"type": "string", "format": "uri"},
            "audio_url": {"type": "string", "format": "uri"},
            "prompt": {"type": "string"},
            "model": {
                "type": "string",
                "enum": [
                    "kling-v1",
                    "kling-v1-6",
                    "kling-v2-master",
                    "kling-v2-1-master",
                    "kling-v2-5-turbo",
                    "kling-v2-6",
                ],
            },
            "duration": {"type": "integer", "enum": [5, 10]},
            "mode": {"type": "string", "enum": ["std", "pro"]},
            "callback_url": {"type": "string", "format": "uri"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_goods_studio": {
        "method": "POST",
        "path": "/kling/goods-studio",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["contents", "settings"],
            "properties": {
                "contents": {
                    "type": "array",
                    "minItems": 2,
                    "items": {
                        "oneOf": [
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["ref_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_title"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 200},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_description"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 2000},
                                },
                            },
                        ]
                    },
                },
                "settings": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                        "aspect_ratio": {"type": "string", "enum": ["9:16", "1:1", "16:9"]},
                        "duration": {"type": "integer", "enum": [15, 30, 60]},
                    },
                    "required": ["aspect_ratio", "duration"],
                },
                "watermark": {"type": "boolean"},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
            },
        },
        "properties": {
            "contents": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["ref_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_title"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 200},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_description"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 2000},
                            },
                        },
                    ]
                },
            },
            "settings": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                    "aspect_ratio": {"type": "string", "enum": ["9:16", "1:1", "16:9"]},
                    "duration": {"type": "integer", "enum": [15, 30, 60]},
                },
                "required": ["aspect_ratio", "duration"],
            },
            "watermark": {"type": "boolean"},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_video_commerce": {
        "method": "POST",
        "path": "/kling/video-commerce",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["contents"],
            "properties": {
                "contents": {
                    "type": "array",
                    "minItems": 2,
                    "items": {
                        "oneOf": [
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["avatar_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["avatar_id"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 128},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["ref_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_title"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 500},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_price"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 256},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_target_audience"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 200},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["goods_selling_point"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 500},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["speech_script"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 2000},
                                },
                            },
                        ]
                    },
                },
                "settings": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                        "aspect_ratio": {"type": "string", "enum": ["9:16", "16:9"]},
                        "allow_polish": {"type": "boolean"},
                        "voice_id": {"type": "string"},
                        "speech_rate": {"type": "number", "enum": [0.8, 1, 1.2]},
                        "action_prompt": {"type": "string", "maxLength": 2500},
                        "bgm_enabled": {"type": "boolean"},
                    },
                },
                "watermark": {"type": "boolean"},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
            },
        },
        "properties": {
            "contents": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["avatar_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["avatar_id"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 128},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["ref_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_title"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 500},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_price"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 256},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_target_audience"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 200},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["goods_selling_point"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 500},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["speech_script"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 2000},
                            },
                        },
                    ]
                },
            },
            "settings": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                    "aspect_ratio": {"type": "string", "enum": ["9:16", "16:9"]},
                    "allow_polish": {"type": "boolean"},
                    "voice_id": {"type": "string"},
                    "speech_rate": {"type": "number", "enum": [0.8, 1, 1.2]},
                    "action_prompt": {"type": "string", "maxLength": 2500},
                    "bgm_enabled": {"type": "boolean"},
                },
            },
            "watermark": {"type": "boolean"},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_virtual_try_on": {
        "method": "POST",
        "path": "/kling/virtual-try-on",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["contents"],
            "properties": {
                "contents": {
                    "type": "array",
                    "minItems": 2,
                    "items": {
                        "oneOf": [
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["product_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["person_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                        ]
                    },
                },
                "settings": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "keep_face": {"type": "boolean"},
                        "keep_pose": {"type": "boolean"},
                        "keep_background": {"type": "boolean"},
                    },
                },
                "watermark": {"type": "boolean"},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
            },
        },
        "properties": {
            "contents": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["product_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["person_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                    ]
                },
            },
            "settings": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "keep_face": {"type": "boolean"},
                    "keep_pose": {"type": "boolean"},
                    "keep_background": {"type": "boolean"},
                },
            },
            "watermark": {"type": "boolean"},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_apparel": {
        "method": "POST",
        "path": "/kling/apparel",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["contents"],
            "properties": {
                "contents": {
                    "type": "array",
                    "minItems": 2,
                    "items": {
                        "oneOf": [
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["product_info"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 2500},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["source_video"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["product_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["model_image"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["bgm"]},
                                    "url": {"type": "string", "minLength": 1},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "voice_id"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["voice"]},
                                    "voice_id": {
                                        "type": "string",
                                        "minLength": 1,
                                        "maxLength": 128,
                                    },
                                },
                            },
                        ]
                    },
                },
                "settings": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                        "aspect_ratio": {
                            "type": "string",
                            "enum": ["9:16", "2:3", "3:4", "1:1", "4:3", "3:2", "16:9", "21:9"],
                        },
                    },
                },
                "watermark": {"type": "boolean"},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
            },
        },
        "properties": {
            "contents": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["product_info"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 2500},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["source_video"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["product_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["model_image"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["bgm"]},
                                "url": {"type": "string", "minLength": 1},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "voice_id"],
                            "properties": {
                                "type": {"type": "string", "enum": ["voice"]},
                                "voice_id": {"type": "string", "minLength": 1, "maxLength": 128},
                            },
                        },
                    ]
                },
            },
            "settings": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "resolution": {"type": "string", "enum": ["720p", "1080p"]},
                    "aspect_ratio": {
                        "type": "string",
                        "enum": ["9:16", "2:3", "3:4", "1:1", "4:3", "3:2", "16:9", "21:9"],
                    },
                },
            },
            "watermark": {"type": "boolean"},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "kling_voices": {
        "method": "POST",
        "path": "/kling/voices",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["list", "presets", "retrieve", "delete", "create"],
                },
                "id": {"type": "string"},
                "page_num": {"type": "integer", "minimum": 1, "maximum": 1000},
                "page_size": {"type": "integer", "minimum": 1, "maximum": 500},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
                "voice_name": {"type": "string", "minLength": 1, "maxLength": 20},
                "voice_url": {"type": "string", "format": "uri"},
            },
        },
        "properties": {
            "action": {
                "type": "string",
                "enum": ["list", "presets", "retrieve", "delete", "create"],
            },
            "id": {"type": "string"},
            "page_num": {"type": "integer", "minimum": 1, "maximum": 1000},
            "page_size": {"type": "integer", "minimum": 1, "maximum": 500},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
            "voice_name": {"type": "string", "minLength": 1, "maxLength": 20},
            "voice_url": {"type": "string", "format": "uri"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "kling_elements": {
        "method": "POST",
        "path": "/kling/elements",
        "operation": "request",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["list", "presets", "retrieve", "delete", "create"],
                },
                "id": {"type": "string"},
                "page_num": {"type": "integer", "minimum": 1, "maximum": 1000},
                "page_size": {"type": "integer", "minimum": 1, "maximum": 500},
                "async": {"type": "boolean"},
                "callback_url": {"type": "string", "format": "uri"},
                "element_name": {"type": "string", "minLength": 1, "maxLength": 20},
                "element_description": {"type": "string", "minLength": 1, "maxLength": 100},
                "reference_type": {"type": "string", "enum": ["image_refer", "video_refer"]},
                "element_voice_id": {"type": "string"},
                "element_image_list": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["frontal_image", "refer_images"],
                    "properties": {
                        "frontal_image": {"type": "string"},
                        "refer_images": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["image_url"],
                                "properties": {"image_url": {"type": "string"}},
                            },
                            "minItems": 1,
                            "maxItems": 3,
                        },
                    },
                },
                "element_video_list": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["refer_videos"],
                    "properties": {
                        "refer_videos": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["video_url"],
                                "properties": {"video_url": {"type": "string", "format": "uri"}},
                            },
                            "minItems": 1,
                            "maxItems": 1,
                        }
                    },
                },
            },
        },
        "properties": {
            "action": {
                "type": "string",
                "enum": ["list", "presets", "retrieve", "delete", "create"],
            },
            "id": {"type": "string"},
            "page_num": {"type": "integer", "minimum": 1, "maximum": 1000},
            "page_size": {"type": "integer", "minimum": 1, "maximum": 500},
            "async": {"type": "boolean"},
            "callback_url": {"type": "string", "format": "uri"},
            "element_name": {"type": "string", "minLength": 1, "maxLength": 20},
            "element_description": {"type": "string", "minLength": 1, "maxLength": 100},
            "reference_type": {"type": "string", "enum": ["image_refer", "video_refer"]},
            "element_voice_id": {"type": "string"},
            "element_image_list": {
                "type": "object",
                "additionalProperties": False,
                "required": ["frontal_image", "refer_images"],
                "properties": {
                    "frontal_image": {"type": "string"},
                    "refer_images": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["image_url"],
                            "properties": {"image_url": {"type": "string"}},
                        },
                        "minItems": 1,
                        "maxItems": 3,
                    },
                },
            },
            "element_video_list": {
                "type": "object",
                "additionalProperties": False,
                "required": ["refer_videos"],
                "properties": {
                    "refer_videos": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["video_url"],
                            "properties": {"video_url": {"type": "string", "format": "uri"}},
                        },
                        "minItems": 1,
                        "maxItems": 1,
                    }
                },
            },
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "kling_task_retrieve": {
        "method": "POST",
        "path": "/kling/tasks",
        "operation": "task",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {"wait_seconds": 0},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "kling_tasks_retrieve_batch": {
        "method": "POST",
        "path": "/kling/tasks",
        "operation": "batch",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
            "required": ["action", "ids"],
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {"action": "retrieve_batch"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
}
