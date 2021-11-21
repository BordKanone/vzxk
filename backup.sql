--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO bordkanone;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO bordkanone;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO bordkanone;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO bordkanone;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO bordkanone;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO bordkanone;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO bordkanone;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO bordkanone;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO bordkanone;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO bordkanone;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO bordkanone;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO bordkanone;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.vzxk_simplecustomers (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    three_name character varying(50) NOT NULL,
    address text NOT NULL,
    avatar character varying(100),
    about character varying(100) NOT NULL
);


ALTER TABLE public.vzxk_simplecustomers OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_groups; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.vzxk_simplecustomers_groups (
    id bigint NOT NULL,
    simplecustomers_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.vzxk_simplecustomers_groups OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.vzxk_simplecustomers_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vzxk_simplecustomers_groups_id_seq OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.vzxk_simplecustomers_groups_id_seq OWNED BY public.vzxk_simplecustomers_groups.id;


--
-- Name: vzxk_simplecustomers_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.vzxk_simplecustomers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vzxk_simplecustomers_id_seq OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.vzxk_simplecustomers_id_seq OWNED BY public.vzxk_simplecustomers.id;


--
-- Name: vzxk_simplecustomers_user_permissions; Type: TABLE; Schema: public; Owner: bordkanone
--

CREATE TABLE public.vzxk_simplecustomers_user_permissions (
    id bigint NOT NULL,
    simplecustomers_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.vzxk_simplecustomers_user_permissions OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bordkanone
--

CREATE SEQUENCE public.vzxk_simplecustomers_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vzxk_simplecustomers_user_permissions_id_seq OWNER TO bordkanone;

--
-- Name: vzxk_simplecustomers_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bordkanone
--

ALTER SEQUENCE public.vzxk_simplecustomers_user_permissions_id_seq OWNED BY public.vzxk_simplecustomers_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: vzxk_simplecustomers id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers ALTER COLUMN id SET DEFAULT nextval('public.vzxk_simplecustomers_id_seq'::regclass);


--
-- Name: vzxk_simplecustomers_groups id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_groups ALTER COLUMN id SET DEFAULT nextval('public.vzxk_simplecustomers_groups_id_seq'::regclass);


--
-- Name: vzxk_simplecustomers_user_permissions id; Type: DEFAULT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.vzxk_simplecustomers_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add Розничный покупатель	6	add_simplecustomers
22	Can change Розничный покупатель	6	change_simplecustomers
23	Can delete Розничный покупатель	6	delete_simplecustomers
24	Can view Розничный покупатель	6	view_simplecustomers
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-11-18 10:03:27.65866+00	2	Anya	1	[{"added": {}}]	6	1
2	2021-11-19 07:46:29.388428+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
3	2021-11-19 08:04:23.095966+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
4	2021-11-19 08:04:34.975183+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
5	2021-11-19 08:34:23.390743+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
6	2021-11-19 08:34:33.763584+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
7	2021-11-19 08:37:34.753441+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
8	2021-11-19 08:37:44.279321+00	2	Anya	2	[{"changed": {"fields": ["\\u0424\\u043e\\u0442\\u043e \\u043f\\u0440\\u043e\\u0444\\u0438\\u043b\\u044f"]}}]	6	1
9	2021-11-19 09:37:54.876534+00	2	Anya	2	[{"changed": {"fields": ["\\u041e\\u043f\\u0438\\u0441\\u0430\\u043d\\u0438\\u0435"]}}]	6	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	vzxk	simplecustomers
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-11-18 09:25:04.408044+00
2	contenttypes	0002_remove_content_type_name	2021-11-18 09:25:04.416067+00
3	auth	0001_initial	2021-11-18 09:25:04.443315+00
4	auth	0002_alter_permission_name_max_length	2021-11-18 09:25:04.447761+00
5	auth	0003_alter_user_email_max_length	2021-11-18 09:25:04.453098+00
6	auth	0004_alter_user_username_opts	2021-11-18 09:25:04.458127+00
7	auth	0005_alter_user_last_login_null	2021-11-18 09:25:04.46231+00
8	auth	0006_require_contenttypes_0002	2021-11-18 09:25:04.463818+00
9	auth	0007_alter_validators_add_error_messages	2021-11-18 09:25:04.467822+00
10	auth	0008_alter_user_username_max_length	2021-11-18 09:25:04.472957+00
11	auth	0009_alter_user_last_name_max_length	2021-11-18 09:25:04.477246+00
12	auth	0010_alter_group_name_max_length	2021-11-18 09:25:04.481964+00
13	auth	0011_update_proxy_permissions	2021-11-18 09:25:04.486372+00
14	auth	0012_alter_user_first_name_max_length	2021-11-18 09:25:04.490543+00
15	vzxk	0001_initial	2021-11-18 09:25:04.516358+00
16	admin	0001_initial	2021-11-18 09:25:04.529914+00
17	admin	0002_logentry_remove_auto_add	2021-11-18 09:25:04.53752+00
18	admin	0003_logentry_add_action_flag_choices	2021-11-18 09:25:04.54305+00
19	sessions	0001_initial	2021-11-18 09:25:04.552101+00
20	vzxk	0002_simplecustomers_avatar	2021-11-19 07:44:57.192053+00
21	vzxk	0003_alter_simplecustomers_avatar	2021-11-19 08:37:06.064839+00
22	vzxk	0004_simplecustomers_about	2021-11-19 09:36:09.793028+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
9zebf1mnvmqikxo8n04ahj9rhpmkelny	.eJxVjEEOwiAQRe_C2pAU2im4dO8ZyAwzSNVAUtpV491tky50-997f1MB1yWHtckcJlZX1anL70YYX1IOwE8sj6pjLcs8kT4UfdKm75XlfTvdv4OMLe-1tUTsJSYGAQbPjDYxDxwNJOwBk0NrZBRyHaEzEfo-RYNm8Ls9gvp8ATMUOWQ:1mndsF:yzHFwbc8hPqe5hwaK3rxtR720HNd5GbJFjo5DdRIl28	2021-12-02 09:38:31.227816+00
\.


--
-- Data for Name: vzxk_simplecustomers; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.vzxk_simplecustomers (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, three_name, address, avatar, about) FROM stdin;
1	pbkdf2_sha256$260000$U97w1Qow9IOvnI6zuFhkxv$Aq/V+CXGuQVRjwfbvBqdWs6hFVVhmpZ/Twmk1vpkuvY=	2021-11-18 09:38:31.225773+00	t	bordkanone			lma709@yandex.ru	t	t	2021-11-18 09:37:55.014595+00			\N	
2	5ed903dF	\N	f	Anya	Анна	Жунина	Lma1@vladhleb.com	f	t	2021-11-18 09:46:05+00	Денисовна	г.Вязники. ул. Механизаторов, д.113	photo_2021-11-16_01-00-01.jpg	Менеджер по работе с сушами
\.


--
-- Data for Name: vzxk_simplecustomers_groups; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.vzxk_simplecustomers_groups (id, simplecustomers_id, group_id) FROM stdin;
\.


--
-- Data for Name: vzxk_simplecustomers_user_permissions; Type: TABLE DATA; Schema: public; Owner: bordkanone
--

COPY public.vzxk_simplecustomers_user_permissions (id, simplecustomers_id, permission_id) FROM stdin;
1	2	20
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 24, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 9, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 6, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: vzxk_simplecustomers_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.vzxk_simplecustomers_groups_id_seq', 1, false);


--
-- Name: vzxk_simplecustomers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.vzxk_simplecustomers_id_seq', 2, true);


--
-- Name: vzxk_simplecustomers_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bordkanone
--

SELECT pg_catalog.setval('public.vzxk_simplecustomers_user_permissions_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: vzxk_simplecustomers_groups vzxk_simplecustomers_gro_simplecustomers_id_group_df4c7935_uniq; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_groups
    ADD CONSTRAINT vzxk_simplecustomers_gro_simplecustomers_id_group_df4c7935_uniq UNIQUE (simplecustomers_id, group_id);


--
-- Name: vzxk_simplecustomers_groups vzxk_simplecustomers_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_groups
    ADD CONSTRAINT vzxk_simplecustomers_groups_pkey PRIMARY KEY (id);


--
-- Name: vzxk_simplecustomers vzxk_simplecustomers_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers
    ADD CONSTRAINT vzxk_simplecustomers_pkey PRIMARY KEY (id);


--
-- Name: vzxk_simplecustomers_user_permissions vzxk_simplecustomers_use_simplecustomers_id_permi_d7c212cb_uniq; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_user_permissions
    ADD CONSTRAINT vzxk_simplecustomers_use_simplecustomers_id_permi_d7c212cb_uniq UNIQUE (simplecustomers_id, permission_id);


--
-- Name: vzxk_simplecustomers_user_permissions vzxk_simplecustomers_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_user_permissions
    ADD CONSTRAINT vzxk_simplecustomers_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: vzxk_simplecustomers vzxk_simplecustomers_username_key; Type: CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers
    ADD CONSTRAINT vzxk_simplecustomers_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: vzxk_simplecustomers_groups_group_id_7b936fce; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX vzxk_simplecustomers_groups_group_id_7b936fce ON public.vzxk_simplecustomers_groups USING btree (group_id);


--
-- Name: vzxk_simplecustomers_groups_simplecustomers_id_2e8b30ad; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX vzxk_simplecustomers_groups_simplecustomers_id_2e8b30ad ON public.vzxk_simplecustomers_groups USING btree (simplecustomers_id);


--
-- Name: vzxk_simplecustomers_user__simplecustomers_id_0bce782b; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX vzxk_simplecustomers_user__simplecustomers_id_0bce782b ON public.vzxk_simplecustomers_user_permissions USING btree (simplecustomers_id);


--
-- Name: vzxk_simplecustomers_user_permissions_permission_id_daf45de0; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX vzxk_simplecustomers_user_permissions_permission_id_daf45de0 ON public.vzxk_simplecustomers_user_permissions USING btree (permission_id);


--
-- Name: vzxk_simplecustomers_username_d343431f_like; Type: INDEX; Schema: public; Owner: bordkanone
--

CREATE INDEX vzxk_simplecustomers_username_d343431f_like ON public.vzxk_simplecustomers USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_vzxk_simplecustomers_id; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_vzxk_simplecustomers_id FOREIGN KEY (user_id) REFERENCES public.vzxk_simplecustomers(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vzxk_simplecustomers_groups vzxk_simplecustomers_groups_group_id_7b936fce_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_groups
    ADD CONSTRAINT vzxk_simplecustomers_groups_group_id_7b936fce_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vzxk_simplecustomers_user_permissions vzxk_simplecustomers_permission_id_daf45de0_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_user_permissions
    ADD CONSTRAINT vzxk_simplecustomers_permission_id_daf45de0_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vzxk_simplecustomers_user_permissions vzxk_simplecustomers_simplecustomers_id_0bce782b_fk_vzxk_simp; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_user_permissions
    ADD CONSTRAINT vzxk_simplecustomers_simplecustomers_id_0bce782b_fk_vzxk_simp FOREIGN KEY (simplecustomers_id) REFERENCES public.vzxk_simplecustomers(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vzxk_simplecustomers_groups vzxk_simplecustomers_simplecustomers_id_2e8b30ad_fk_vzxk_simp; Type: FK CONSTRAINT; Schema: public; Owner: bordkanone
--

ALTER TABLE ONLY public.vzxk_simplecustomers_groups
    ADD CONSTRAINT vzxk_simplecustomers_simplecustomers_id_2e8b30ad_fk_vzxk_simp FOREIGN KEY (simplecustomers_id) REFERENCES public.vzxk_simplecustomers(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

