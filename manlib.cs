using System;

public delegate bool CallBack(int iParam, int lParam, string sParam, float fParam, double dParam);
public class ManLib
{
    public static string Bootstrap()
    {
        return "ManLib Bootstrapped!";
    }

    public static string BootstrapCB(CallBack cb)
    {
        bool ok = cb(1, 2, "some string", 1.0f, 2.0);
        if( ok )
            return "Ok";
        return "Failure";
    }
}
