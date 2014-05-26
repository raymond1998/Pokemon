// PgbarLoader.cpp : ����Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include "PgbarLoader.h"

#define MAX_LOADSTRING 100

// ȫ�ֱ���: 
HINSTANCE hInst;								// ��ǰʵ��
HWND g_hWnd;
HWND g_pbar;
TCHAR szTitle[MAX_LOADSTRING];					// �������ı�
TCHAR szWindowClass[MAX_LOADSTRING];			// ����������
std::wstring g_title{};
std::wstring g_event_name{};
TCHAR szEventName[MAX_LOADSTRING];				// Event name IDS_LOADER_EVENT

class WindowsEvent
{
public:
	WindowsEvent(){};
	WindowsEvent(LPSECURITY_ATTRIBUTES lpEventAttributes, bool bManualReset, bool bInitialState, LPCWSTR lpName)
	{
		m_evt = CreateEvent(lpEventAttributes, bManualReset, bInitialState, lpName);
	};

	void init(LPSECURITY_ATTRIBUTES lpEventAttributes, bool bManualReset, bool bInitialState, LPCWSTR lpName)
	{
		release();
		m_evt = CreateEvent(lpEventAttributes, bManualReset, bInitialState, lpName);
	};

	void release(bool resetevt = true);

	~WindowsEvent()
	{
		release();
	};

	HANDLE m_evt = nullptr;
};

void WindowsEvent::release(bool resetevt)
{
	if (m_evt != nullptr)
	{
		if (resetevt) ResetEvent(m_evt);
		CloseHandle(m_evt);
		m_evt = nullptr;
	}
}

WindowsEvent g_evt{};

// �˴���ģ���а����ĺ�����ǰ������: 
ATOM				MyRegisterClass(HINSTANCE hInstance);
BOOL				InitInstance(HINSTANCE, int);
LRESULT CALLBACK	WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK	About(HWND, UINT, WPARAM, LPARAM);
HWND pgbar(HWND hwndParent);
void Release();

int APIENTRY _tWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPTSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
	UNREFERENCED_PARAMETER(hPrevInstance);
	UNREFERENCED_PARAMETER(lpCmdLine);

	// ��ʼ��ȫ���ַ���
	LoadString(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
	LoadString(hInstance, IDC_PGBARLOADER, szWindowClass, MAX_LOADSTRING);
	LoadString(hInstance, IDS_LOADER_EVENT, szEventName, MAX_LOADSTRING);
	int argc{0};
	LPWSTR* argv{ CommandLineToArgvW(GetCommandLine(), &argc) };

	if (argc >= 3)
	{
		g_title = argv[1];
		g_event_name = argv[2];
	}
	
	switch (argc)
	{
	case 2:
		g_title = argv[1];
		g_event_name = szEventName;
		break;
	case 1:
		g_title = szTitle;
		g_event_name = szEventName;
	}

	std::wstring rep{ '\x1f' };
	std::wstring space{ ' ' };
	std::size_t found{};
	do {
		found = g_title.find(rep);
		if (found != std::wstring::npos) g_title.replace(found, 1, space);
	} while (found != std::wstring::npos);


	MyRegisterClass(hInstance);

	// TODO:  �ڴ˷��ô��롣
	g_evt.init(NULL, TRUE, FALSE, g_event_name.c_str());
	if (!g_evt.m_evt) return FALSE;

	// ִ��Ӧ�ó����ʼ��: 
	if (!InitInstance (hInstance, nCmdShow))
	{
		return FALSE;
	}

	g_pbar = pgbar(g_hWnd);
	MSG msg;
	// ����Ϣѭ��: 
	while (GetMessage(&msg, NULL, 0, 0))
	{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
	}

	return (int) msg.wParam;
}



//
//  ����:  MyRegisterClass()
//
//  Ŀ��:  ע�ᴰ���ࡣ
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
	WNDCLASSEX wcex;

	wcex.cbSize = sizeof(WNDCLASSEX);

	wcex.style = NULL;
	wcex.lpfnWndProc	= WndProc;
	wcex.cbClsExtra		= 0;
	wcex.cbWndExtra		= 0;
	wcex.hInstance		= hInstance;
	wcex.hIcon			= LoadIcon(hInstance, MAKEINTRESOURCE(IDI_PGBARLOADER));
	wcex.hCursor		= LoadCursor(NULL, IDC_ARROW);
	wcex.hbrBackground	= (HBRUSH)(COLOR_WINDOW+1);
	wcex.lpszMenuName = 0;
	wcex.lpszClassName	= szWindowClass;
	wcex.hIconSm		= LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

	return RegisterClassEx(&wcex);
}

//
//   ����:  InitInstance(HINSTANCE, int)
//
//   Ŀ��:  ����ʵ�����������������
//
//   ע��: 
//
//        �ڴ˺����У�������ȫ�ֱ����б���ʵ�������
//        ��������ʾ�����򴰿ڡ�
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   HWND hWnd;

   hInst = hInstance; // ��ʵ������洢��ȫ�ֱ�����
   int cyVScroll = GetSystemMetrics(SM_CYVSCROLL);
   RECT rect;
   rect.right = 400;
   rect.bottom = cyVScroll;
   rect.left = 0;
   rect.top = 0;
   AdjustWindowRect(&rect, WS_VISIBLE | WS_CAPTION | WS_OVERLAPPED, false);

   int sx{ GetSystemMetrics(SM_CXSCREEN) };
   int sy{ GetSystemMetrics(SM_CYSCREEN) };
   int x{ rect.right - rect.left };
   int y{ rect.bottom - rect.top };
   hWnd = CreateWindowEx(WS_EX_TOPMOST, szWindowClass, g_title.c_str(), WS_VISIBLE | WS_CAPTION | WS_OVERLAPPED,
	   (sx - x) / 2, (sy - y) / 2, rect.right - rect.left, rect.bottom - rect.top, NULL, NULL, hInstance, NULL);

   if (!hWnd)
   {
	   
      return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);
   g_hWnd = hWnd;

   return TRUE;
}

//
//  ����:  WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  Ŀ��:    ���������ڵ���Ϣ��
//
//  WM_COMMAND	- ����Ӧ�ó���˵�
//  WM_PAINT	- ����������
//  WM_DESTROY	- �����˳���Ϣ������
//
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	PAINTSTRUCT ps;
	HDC hdc;

	switch (WaitForSingleObject(g_evt.m_evt, 0))
	{
	case WAIT_TIMEOUT:
		break;
	default:
		PostQuitMessage(0);
		return 0;
	}

	switch (message)
	{
	case WM_PAINT:
		hdc = BeginPaint(hWnd, &ps);
		// TODO:  �ڴ���������ͼ����...
		EndPaint(hWnd, &ps);
		break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd, message, wParam, lParam);
	}
	return 0;
}


HWND pgbar(HWND hwndParent)
{
	RECT rcClient;  // Client area of parent window.
	int cyVScroll;  // Height of scroll bar arrow.
	HWND hwndPB;    // Handle of progress bar.

	// Ensure that the common control DLL is loaded, and create a progress bar 
	// along the bottom of the client area of the parent window. 
	//
	// Base the height of the progress bar on the height of a scroll bar arrow.

	GetClientRect(hwndParent, &rcClient);

	cyVScroll = GetSystemMetrics(SM_CYVSCROLL);

	hwndPB = CreateWindowEx(0, PROGRESS_CLASS, (LPTSTR)NULL,
		WS_CHILD | WS_VISIBLE | PBS_MARQUEE, rcClient.left,
		rcClient.bottom - cyVScroll,
		rcClient.right, cyVScroll,
		hwndParent, (HMENU)0, hInst, NULL);


	// Set the marguee
	SendMessage(hwndPB, (UINT)PBM_SETMARQUEE, (WPARAM)1, (LPARAM)NULL);

	return hwndPB;
}

