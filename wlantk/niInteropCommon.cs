// Contains types that are common among RF Toolkits and Modular Instruments wrappers.
using System;
using System.Runtime.InteropServices;

namespace NationalInstruments.ModularInstruments.Interop
{
    /// <summary>
    /// 
    /// </summary>
    [StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 8)]
    public struct niComplexNumber
    {
/// <summary>
/// 
/// </summary>
        public double Real;
        /// <summary>
        /// 
        /// </summary>
        public double Imaginary;

    }
    /// <summary>
    /// 
    /// </summary>
    [StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 8)]
    public struct niComplexI16
    {
        /// <summary>
        /// 
        /// </summary>
        public short Real;
        /// <summary>
        /// 
        /// </summary>
        public short Imaginary;

    }
    /// <summary>
    /// 
    /// </summary>
    [StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 8)]
    public struct niComplexNumberF32
    {
        /// <summary>
        /// 
        /// </summary>
        public float Real;
        /// <summary>
        /// 
        /// </summary>
        public float Imaginary;

    }

    /// <summary>
    /// 
    /// </summary>
    [StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential, Pack = 8)]
    [Obsolete("This struct is obsolete. Use struct niComplexNumberF32.")]    
    public struct niComplexF32
    {
        /// <summary>
        /// 
        /// </summary>
        public float Real;
        /// <summary>
        /// 
        /// </summary>
        public float Imaginary;

    }
}
